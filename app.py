import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset
df = pd.read_csv("data/daily_sales_data_0.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Convert region to lowercase
df["region"] = df["region"].str.lower()

# 🔥 CREATE SALES COLUMN (IMPORTANT FIX)
df["sales"] = df["quantity"] * df["price"]

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Pink Morsel Sales Dashboard", style={"textAlign": "center"}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-graph")

])
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # 🔥 REMOVE TIME PART
    filtered_df["date_only"] = filtered_df["date"].dt.date

    # Group by date_only
    grouped = (
        filtered_df
        .groupby("date_only", as_index=False)
        .agg({"sales": "sum"})
        .sort_values("date_only")
    )

    fig = px.line(
        grouped,
        x="date_only",
        y="sales",
        title="Sales Over Time",
        labels={"date_only": "Date", "sales": "Total Sales"}
    )

    return fig



if __name__ == "__main__":
    app.run(debug=True)

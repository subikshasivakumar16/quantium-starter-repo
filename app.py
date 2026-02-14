# app.py
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# ---------------------------
# Load and prepare dataset
# ---------------------------
df = pd.read_csv("data/daily_sales_data_0.csv")

# Clean column names
df.columns = df.columns.str.lower().str.strip()

# Convert date to datetime.date
df["date"] = pd.to_datetime(df["date"]).dt.date

# Lowercase region values
df["region"] = df["region"].str.lower()

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Group once globally
df_grouped = df.groupby(["date", "region"], as_index=False)["sales"].sum()

# ---------------------------
# Initialize Dash app
# ---------------------------
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

# ---------------------------
# Layout
# ---------------------------
app.layout = html.Div([

    # Header
    html.H1(
        "Pink Morsel Sales Dashboard",
        id="dashboard-header",  # ID for testing
        style={"textAlign": "center", "marginBottom": "30px"}
    ),

    # Region Picker (RadioItems)
    dcc.RadioItems(
        id="region-picker",  # ID for testing
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "30px"}
    ),

    # Graph
    dcc.Graph(
        id="sales-graph",  # ID for testing
    )
])

# ---------------------------
# Callback to update graph
# ---------------------------
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):
    # Filter data based on selection
    if selected_region == "all":
        data = df_grouped.groupby("date", as_index=False)["sales"].sum()
    else:
        data = df_grouped[df_grouped["region"] == selected_region]

    # Create figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data["date"],
        y=data["sales"],
        mode="lines+markers",
        name="Sales"
    ))

    # Layout settings
    fig.update_layout(
        title="Sales Over Time",
        xaxis_title="Date",
        yaxis_title="Total Sales",
        template="plotly_white"
    )

    return fig

# ---------------------------
# Run the server
# ---------------------------
if __name__ == "__main__":
    app.run_server(debug=True)

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group by date and sum sales
df_grouped = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Analysis of Pink Morsels"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)

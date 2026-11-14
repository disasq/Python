from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("spacex_launch_dash.csv")
app = Dash(__name__)

app.layout = html.Div([
    html.H2("SpaceX Falcon 9 Launch Dashboard"),
    dcc.Dropdown(df["Site"].unique(), "ALL", id="site"),
    dcc.Graph(id="success-pie"),
    dcc.RangeSlider(0, 10000, 1000, value=[0, 10000], id="payload"),
    dcc.Graph(id="payload-scatter"),
])

@app.callback(
    Output("success-pie", "figure"),
    Output("payload-scatter", "figure"),
    Input("site", "value"),
    Input("payload", "value"),
)
def update(site, payload):
    data = df if site == "ALL" else df[df["Site"] == site]
    data = data[(data["Payload Mass (kg)"] >= payload[0]) & (data["Payload Mass (kg)"] <= payload[1])]
    pie = px.pie(data, names="class", title="Landing success")
    scatter = px.scatter(data, x="Payload Mass (kg)", y="class", color="Booster Version Category")
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)

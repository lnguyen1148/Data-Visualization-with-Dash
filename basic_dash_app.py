import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

# Read in data
data = pd.read_csv("ukr_asylum.csv", usecols=["Year", "Asylum-seekers"])

# Create a plotly figure for dcc.Graph()
fig = px.line(
    data,
    x="Year",
    y=["Asylum-seekers"],
    title="Asylum seekers from Ukraine 2016-2021",
    color_discrete_map={"Asylum-seekers": "gold"}
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Year",
    yaxis_title="Asylum seekers",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    )
)

app = dash.Dash(__name__)
app.title = "Asylum seekers from Ukraine 2016-2021"

app.layout = html.Div(
    id="app-container",
    children=[
        html.H1("Asylum seekers from Ukraine 2016-2021"),
        html.P("Data extracted from the UN Refugee Agency"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)


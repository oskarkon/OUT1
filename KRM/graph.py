import dash
from datetime import datetime
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('D:\\prog\\Python\\jupyter\\input\\data.csv')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph=1'),
    dcc.Slider(
        id='slider-a',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),
        marks={str(year): str(year) for year in df.year.unique()},
        step=5
    )
])

def update_graph(selected_year):
    dff = df.query(f'year=={selected_year}')
     


if __name__ == '__main__':
    app.run_server(debug=True)

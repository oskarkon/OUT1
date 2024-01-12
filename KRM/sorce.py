import dash
from dash import dash_table
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output

def extract():
    df = pd.read_csv('D:\prog\Python\jupyter\input\pokemon.csv')
    return df



def wykres():

    df=extract()
    return html.Div([dcc.Dropdown(id = "input",options=['Grass','Fire']
    ),
        dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Name,
                    y=df.Attack
                )
            ]
        )

    ),
    html.Div([
        dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    ])
        ])

    tooltip_data=[
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in df.to_dict('records')
        ],
    tooltip_duration=None


app = dash.Dash(__name__)
app.layout = html.Div([html.Label('tabelka'),wykres()



])


if __name__ == "__main__":
    app.run_server(debug=True)


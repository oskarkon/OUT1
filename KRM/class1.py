import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    className='row',
    children=[
        html.Div(
            className='col-6',
            children=[
                dcc.Graph(
                    id='graph1',
                    figure={
                        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Chart 1'}],
                        'layout': {'title': 'Chart 1'},
                    },
                ),
            ],
        ),
        html.Div(
            className='col-6',
            children=[
                dcc.Graph(
                    id='graph2',
                    figure={
                        'data': [{'x': [1, 2, 3], 'y': [2, 4, 1], 'type': 'bar', 'name': 'Chart 2'}],
                        'layout': {'title': 'Chart 2'},
                    },
                ),
            ],
        ),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)

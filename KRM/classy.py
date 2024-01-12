import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            style={'display': 'flex'},
            children=[
                html.Div(
                    style={'flex': '80%'},
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
                    style={'flex': '80%'},
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
        ),
        html.Div(
            style={'display': 'flex', 'justify-content': 'center', 'margin-top': '5mm'},
            children=[
                dcc.Input(id='input1', type='number', placeholder='Input 1', value=500, step=100),
            ],
        ),
        html.Div(
            style={'display': 'flex', 'justify-content': 'center', 'margin-top': '5mm'},
            children=[
                dcc.Input(id='input2', type='number', placeholder='Input 2', value=500, step=100),
            ],
        ),
        html.Div(
            style={'display': 'flex'},
            children=[
                html.Div(
                    style={'flex': '30%'},
                    children=[
                        dcc.Graph(
                            id='graph3',
                            figure={
                                'data': [{'x': [1, 2, 3], 'y': [3, 2, 4], 'type': 'bar', 'name': 'Chart 3'}],
                                'layout': {'title': 'Chart 3'},
                            },
                        ),
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)

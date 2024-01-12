import dash
from dash import dash_table
import pandas as pd
import timeit
# Przykładowe DataFrame 1
data1 = {'ID': [1, 2, 3],
         'NAME': ['A', 'B', 'C']}
df1 = pd.DataFrame(data1)

# Przykładowe DataFrame 2
data2 = {'NAME': ['A', 'B', 'C'],
         'TOOLTIP': ['Info A', 'Info B', 'Info C']}
df2 = pd.DataFrame(data2)

# Inicjalizacja aplikacji Dash
app = dash.Dash(__name__)

# Tworzenie tabeli
app.layout = dash.html.Div([
    dash_table.DataTable(
        id='datatable',
        columns=[
            {'name': 'ID', 'id': 'ID'},
            {'name': 'NAME', 'id': 'NAME'}
        ],
        data=df1.to_dict('records'),
        tooltip_data=[
            {
                column: {'value': row['NAME']}
                for column in ['NAME']
            }
            for row in df2.to_dict('records')
        ],
        tooltip_duration=None,
        style_table={'height': '300px', 'overflowY': 'auto'}
    )
])

@app.callback(
    dash.dependencies.Output('datatable', 'tooltip'),
    [dash.dependencies.Input('datatable', 'data')]
)
def update_tooltip(data):
    tooltip_dict = {}
    for row in data:
        name_value = row['NAME']
        tooltip = df2[df2['NAME'] == name_value]['TOOLTIP'].values[0]
        tooltip_dict[row['id']] = tooltip
    return tooltip_dict

if __name__ == '__main__':
    app.run_server(debug=True)

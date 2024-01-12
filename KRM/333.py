import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

# Main data table
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Location': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Tooltip data
tooltip_data = {
    'Name': ['Alice', 'Alice', 'Bob', 'Charlie'],
    'Tooltip': ['This is Alice 1\'s tooltip', 'This is Alice 2\'s tooltip', 'This is Bob\'s tooltip',
                'This is Charlie\'s tooltip']
}

tooltip_df = pd.DataFrame(tooltip_data)

# Create a dictionary to store tooltips for each row
tooltip_dict = {}
for _, row in tooltip_df.iterrows():
    name = row['Name']
    tooltip = row['Tooltip']
    if name not in tooltip_dict:
        tooltip_dict[name] = []
    tooltip_dict[name].append(tooltip)

app.layout = html.Div([
    html.H1("Main Table"),
    dash_table.DataTable(
        id='main-datatable',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        editable=True,
        row_deletable=True
    ),

    html.Hr(),

    html.Div(id='tooltip-container')
])


@app.callback(
    Output("tooltip-container", "children"),
    [Input("main-datatable", "active_cell")],
    prevent_initial_call=True,
)
def update_tooltip_table(active_cell):
    if not active_cell:
        return []

    row_id = active_cell['row']
    name = df.loc[row_id, 'Name']
    tooltips = tooltip_dict.get(name, [])

    tooltip_table = []
    for tooltip in tooltips:
        tooltip_table.append(html.P(tooltip))

    return tooltip_table


if __name__ == '__main__':
    app.run_server(debug=True)

import pandas as pd
from dash import Dash, html, dcc, dash_table,Input,Output
import plotly.express as px

df=pd.read_csv('D:\\prog\\Python\\jupyter\\input\\pokemon.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
            html.Div(className='row',children='Pokemonki'),
            html.Div(className='row',children=[dcc.RadioItems(options=['Generation','Attack','Defense','HP','Total'], id='radio')]),
            html.Div(className='6 columns',
                     children=[
            dash_table.DataTable(data=df.to_dict('records'),page_size=10),
            dcc.Graph(figure={}, id='wykres')])


            ])



@app.callback(
            Output(component_id='wykres',component_property='figure'),

            Input(component_id='radio',component_property='value')
)
def update_wykres(radio):
    fig = px.histogram(df, x='Name',y=radio)
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
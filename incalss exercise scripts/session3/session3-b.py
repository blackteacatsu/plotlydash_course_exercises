from dash import Dash, html, dcc, Input, Output, callback, no_update
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

columnDefs = [
    { 'field': 'country' },
    { 'field': 'pop' },
    { 'field': 'continent'},
    { 'field': 'lifeExp' },
    { 'field': 'gdpPercap' }
]

grid = dag.AgGrid(
    id="tabular-data",
    rowData=df.to_dict("records"),
    columnDefs=columnDefs,
)

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='radio-buton'),
    grid,
    dcc.Graph(figure={}, id='my-scatter', hoverData=None)
])

# Add controls to build the interaction
@callback(
    Output(component_id='my-scatter', component_property='figure'),
    Input(component_id='radio-buton', component_property='value')
)
def update_graph(yaxis_chosen):
    fig = px.scatter(df, x='gdpPercap', y=yaxis_chosen)
    return fig


@callback(
    Output(component_id='tabular-data', component_property='rowData'),
    Output(component_id='tabular-data', component_property='columnDefs'),
    Input(component_id='my-scatter', component_property='clickData') # or use component_property='hoverData'
)
def update_table(click_data):
    # print(hover_data)
    x_axis_data = click_data['points'][0]['x']
    # print(f'gdp per capita: {x_axis_data}')
    dff = df[df.gdpPercap == x_axis_data]
    print(dff)
    return dff.to_dict("records"), columnDefs

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

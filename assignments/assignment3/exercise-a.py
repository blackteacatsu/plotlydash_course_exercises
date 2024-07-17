# assignment from session 3
# link to google doc: 
# https://docs.google.com/document/d/1YiGWjwIOi28dOU1geVP3LBW2BVO5vJiZw-1wGwfiIfA/edit


# Import libraries
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px


# Using WasmDash and the 2011_us_ag_exports.csv dataset,
#  we will use the graph’s hoverData property to extra the country hovered over 
# and build a Dash Ag Grid with that country’s export data. 


# Import csv files from github
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

# Define app
app = Dash(__name__)

# App layout
app.layout = html.Div([
   html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
   dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
   dcc.Graph(id="graph1"),
   html.Div(id='table-here'),
])

#callback decorator
@callback(
   Output(component_id='graph1', component_property='figure'),
   Input(component_id='state-dropdown', component_property='value'),
)

#callback function
def update_graph(states_selected):
   df_country = df[df.state.isin(states_selected)]
   fig1 = px.bar(data_frame=df_country, x='state', y=['beef','pork','fruits fresh'])
   return fig1

@callback(
   Output(component_id='table-here', component_property='children'),
   Input(component_id='graph1', component_property='hoverData'),
   prevent_initial_call = True
)
def hover_func(data_hovered):
   print(data_hovered)
   print(type(data_hovered))
   dff = df[df.state == data_hovered['points'][0]['x']]
   grid = dag.AgGrid(rowData=dff.to_dict('records'), 
                     columnDefs=[{'field': i} for i in dff.columns],
                     defaultColDef={'resizable': True},
                     #columnSize='sizeToFit',
                     #dashGridOptions={'pagination':True, 'paginationAutoPageSize': True}
                    )
   return grid

# Run the app
if __name__ == '__main__':
  app.run(debug=True)
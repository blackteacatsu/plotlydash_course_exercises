from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
   html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
   dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
   dbc.Button('Submit', id='state-button', n_clicks=0),
   dcc.Graph(id="graph1"),
])

@app.callback(
   Output(component_id='graph1', component_property='figure'),
   Input(component_id='state-button',component_property='n_clicks'),
   State(component_id='state-dropdown', component_property='value'),
)
def update_graph(_, states_selected):
   df_states = df[df.state.isin(states_selected)]
   fig1 = px.bar(data_frame=df_states, x='state', y=['beef','pork','fruits fresh'])
   return fig1


if __name__ == '__main__':
  app.run(debug=True)
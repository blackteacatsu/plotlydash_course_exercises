# assignment from session 1
# link to google doc: 
# https://docs.google.com/document/d/1gUpMaA4pLiZEh5otMlARkbXLOaYENwdZmvDomXj_hTA/edit
# link to resource page:
# https://docs.google.com/document/d/19wtalaIomUhfky-gBvFvjtQdyWh_CRiJUSnzAbxhcHI/edit


# Import libraries
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px

# Define app
app = Dash(__name__)

# Import data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv")


# App layout
app.layout = html.Div([
    # Above the dropdown, add an html.Div, and assign to the id property the string “my-title”. 
    # Add your own title to the children property of the html.Div. 
    html.Div(children="my-title", id="title"),
    # A Dropdown that uses column state as the dropdown options. Then, assign “Alabama” as the initial value. The dropdown id should equal “state-dropdown”.
    dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama", "Arkansas"], multi=True),
    # Below the dropdown, add an empty dcc.Graph. The id of the graph component should be “graph1”. 
    dcc.Graph(id="graph-1")
    ])



# Add a callback decorator that takes the value of the dcc.Dropdown as an Input argument 
# and the figure of the dcc.Graph as an Output argument. 

@callback(
    Output(component_id="graph-1",component_property="figure"),
    Input(component_id="state-dropdown", component_property="value")
)

# Callback function:
# The function should take an argument called “state_selected”. 
# Use pandas to filter the original dataframe (df) so that only rows with the “state_selected” remain in the new dataframe. 
# Name the new dataframe “df_country”. 

def graph(state_selected):

    # Get the name of the selected state from terminal
    # print(state_selected)

    df_country = df[df.state.isin(state_selected)]
    print(df_country)
    fig =  px.bar(data_frame=df_country, x="state", y=['beef','pork','fruits fresh'])
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
# assignment from session 1
# link to google doc: 
# https://docs.google.com/document/d/1XtS0cLxe7GT5WoZ6U7Qfk008aw1fazYRvrbKO29G3BM/edit
# link to resource page:
# https://docs.google.com/document/d/1lmSTdRgxUZ6jZRED9UJtLkuXgEQN_3R8u4F3nU6bChQ/edit


# Import libraries
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px

# Initialize the app
app = Dash(__name__)

# read data form
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

# create new scatter plot
my_scatter_plot = px.scatter(df, x="V", y="S")


# App layout
app.layout = html.Div([dcc.Graph(figure=my_scatter_plot)])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


# assignment from session 1
# link to google doc: 
# https://docs.google.com/document/d/1XtS0cLxe7GT5WoZ6U7Qfk008aw1fazYRvrbKO29G3BM/edit
# link to resource page:
# https://docs.google.com/document/d/1lmSTdRgxUZ6jZRED9UJtLkuXgEQN_3R8u4F3nU6bChQ/edit


# Import libraries
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import dash_ag_grid as dag

# Initialize the app
app = Dash(__name__)

# read data form
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

# The Dash AG Grid should represent the complete dataset with all its columns.
# grid = dag.AgGrid(id="my-table", rowData=df.to_dict("records"), columnDefs=[{"field": i} for i in df.columns]),

# Using Pagination, add automatic pagination to Dash AG Grid and make sure all columns fit 
# into the screen with no horizontal scroll bar (using the columnSize property). 
grid = dag.AgGrid(
    id="my-table",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    columnSize="sizeToFit",
    dashGridOptions={"pagination":True},
)


# App layout
app.layout = html.Div([grid])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
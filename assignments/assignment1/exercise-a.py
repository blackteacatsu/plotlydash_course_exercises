# assignment from session 1
# link to google doc: 
# https://docs.google.com/document/d/1XtS0cLxe7GT5WoZ6U7Qfk008aw1fazYRvrbKO29G3BM/edit
# link to resource page:
# https://docs.google.com/document/d/1lmSTdRgxUZ6jZRED9UJtLkuXgEQN_3R8u4F3nU6bChQ/edit


# Import libraries
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd

# Initialize the app
app = Dash(__name__)

# read data form
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

# App layout
app.layout = html.Div([
  
  # A Dropdown that uses the column brand as the dropdown options. 
  # Make sure the brand names are unique (do not repeat themselves). Then, assign “Revlon” as the initial value.
  dcc.Dropdown(options = df.brand.unique(), value = "Revlon"),

  html.Hr(),
  
  # A RadioItems component in which the values from the column named group are assigned to the options property. 
  # The options should be unique and sorted from 0 to 7.
  ## dcc.RadioItems(options = sorted(df.group.unique())),
  
  # Update the options property of the RadioItems component so that the values (of the options) 
  # represent numbers from 0 to 7, but the labels are their respective strings (see Readme-shades for the strings).
  dcc.RadioItems(options = [{"label": " Fenty Beauty's PRO FILT'R Foundation Only", "value": "0"},
                            {"label": " Make Up For Ever's Ultra HD Foundation Only", "value": "1"},
                            {"label": " US Best Sellers", "value": "2"},
                            {"label": " BIPOC-recommended Brands with BIPOC Founders", "value": "3"},
                            {"label": " BIPOC-recommended Brands with White Founders", "value": "4"},
                            {"label": " Nigerian Best Sellers", "value": "5"},
                            {"label": " Japanese Best Sellers", "value": "6"},
                            {"label": " Indian Best Sellers", "value": "7"}
                            ], value="3"),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

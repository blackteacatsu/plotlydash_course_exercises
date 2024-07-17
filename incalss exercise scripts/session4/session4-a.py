#import micropip
#await micropip.install('dash-bootstrap-components')
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.CYBORG]
)

'''Code from Example 1.py:'''
'''app.layout = dbc.Container([
    html.H1("Dash Bootstrap Alerts"),
    #dbc.Alert("Hello, Bootstrap!", className="m-5", is_open=True, duration=4000),
    dbc.Button("Submit",color='primary', className='mt-5 border rounded-pill'),
])'''

'''Code from annex_a.py: '''
app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
        dbc.Row(
            [# Each row has 12 units 
                #dbc.Col(dbc.Alert("One of three columns"), width=4),
                #dbc.Col(dbc.Alert("One of three columns"), width=4),
               #dbc.Col(dbc.Alert("One of three columns"), width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Alert("One of four columns"), width=12, md=3),
                dbc.Col(dbc.Alert("One of four columns"), width=12, md=3),
                dbc.Col(dbc.Alert("One of four columns"), width=12, md=3),
                dbc.Col(dbc.Alert("One of four columns"), width=12, md=3),
            ]
        )
])

if __name__ == "__main__":
    app.run_server()
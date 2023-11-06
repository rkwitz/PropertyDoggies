import dash
from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps import navigation
import os


'''
Dash in a nutshell

Create pages like this
* Containers
* Functions
* Callbacks

All three should be separated like below.

Containers are dbc, dash, html, etc; basically just front end containers that define the layout of the page
Functions just being logic used in callbacks
Callbacks are decorated functions that fire when a callback is fired (button is pressed + many other interactions)

So basically use callbacks to update containers, and use functions for repeating stuff

'''

# Containers

dash.register_page(__name__, path='/data',
                   title="Data", description="Here we should have input data handling")

download_button = dbc.Container([
    dbc.Col(children=[
        dbc.Row(children=[
            html.Button("Click here to download", id='btn-download-resume'),
            dcc.Download(id="download-something")
        ])
    ])

])

layout = html.Div(children=[
    navigation.navbar,
    download_button
])

# Functions
def foo():
    print("example function in callback")

# Callbacks
# They must follow the form of this
# @callback( Output(object name of container to present return, where to return within the container object

@callback(
    Output("download-something", "data"),
    [Input("btn-download-resume", "n_clicks")],
    prevent_initial_callback=True
)
def download_resume(n_clicks):
    foo()
    # deprecated file path for download button
    return dcc.send_file("\\assets\\resume\\"+os.listdir("\\assets\\resume\\"))



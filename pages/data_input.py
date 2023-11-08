import dash
from dash import html, callback, Input, Output, dash_table, State, dcc
import dash_bootstrap_components as dbc
from apps import navigation
import os
import datetime
import base64
import io
import pandas as pd


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
        ]),
        dbc.Row(children=[
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id='output-data-upload'),
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


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])
# Callbacks
# They must follow the form of this
# @callback( Output(object name of container to present return, where to return within the container object



@callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@callback(
    Output("download-something", "data"),
    [Input("btn-download-resume", "n_clicks")],
    prevent_initial_callback=True
)
def download_resume(n_clicks):
    foo()
    # deprecated file path for download button
    return dcc.send_file("\\assets\\resume\\"+os.listdir("\\assets\\resume\\"))



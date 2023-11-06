import dash
from dash import html
import dash_bootstrap_components as dbc
from apps import navigation


dash.register_page(__name__, path='/',
                   title="Property Doggies", description="When you're here you're family")

layout = html.Div(children=[
    navigation.navbar,
    html.H2(children="Welcome to Property Doggies")
])


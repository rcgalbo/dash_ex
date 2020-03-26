from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div(
    [
        html.H3('dash 1 - map'),
        html.Iframe(className='map', srcDoc=open('assets/hospital_map.html').read()), 
        html.Div(id='app-1-display-value'),
        dcc.Link('Go to dash 2 - data', href='/dash2'),
        html.Div(),
        dcc.Link('Return Home', href='/'),
    ]
)


from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div([
    html.H3('Home Page'),
    dcc.Dropdown(
        id='home-dropdown',
        options=[
            {'label': 'Home - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='home-display-value'),
    dcc.Link('Go to dash1', href='/dash1'),
    html.Div(),
    dcc.Link('Go to dash2', href='/dashp2')
])


@app.callback(
    Output('home-display-value', 'children'),
    [Input('home-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

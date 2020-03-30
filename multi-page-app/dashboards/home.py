from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

from app import hospitals
# define homepage layout
layout = html.Div(
    className='container',
    children=[
        html.H3('Home Page - US Hospital Data'),
        html.P('Select state from dropdown to get the number of hospitals'),
        html.Div(id='home-display-value', className='col-8'),
        dcc.Dropdown(
        id='home-dropdown',
        className='col-8',
        options=[
            {'label': '{}'.format(i), 'value': i}
            for i in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
                    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
            ],
        ),
        dcc.Link('Go to dash1 - map', href='/dash1'),
        html.Div(),
        dcc.Link('Go to dash2 - data', href='/dash2'),
    ]
)


@app.callback(
    Output('home-display-value', 'children'), [Input('home-dropdown', 'value')]
)
def display_value(value):
    if value == None:
        val = 0
    else:
        val = hospitals[hospitals.STATE == value].shape[0]
    return 'The state you have selected has {} hospitals'.format(val)

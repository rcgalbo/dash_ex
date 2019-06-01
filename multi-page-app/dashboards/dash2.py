from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div(
    [
        html.H3('App 2'),
        dcc.Dropdown(
            id='app-2-dropdown',
            options=[
                {'label': 'App 2 - {}'.format(i), 'value': i}
                for i in ['NYC', 'MTL', 'LA']
            ],
        ),
        html.Div(id='app-2-display-value'),
        dcc.Link('Go to dash 1', href='/dash1'),
        html.Div(),
        dcc.Link('Return Home', href='/'),
    ]
)


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')],
)
def display_value(value):
    return 'You have selected "{}"'.format(value)

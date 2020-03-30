from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table

from app import app
from app import hospitals

layout = html.Div(className='container',
    children = [
        html.H3('dash 2 - data'),
        dash_table.DataTable(id='hospitals',
            columns = [{'name':i,'id':i} for i in hospitals.columns],
            data=hospitals.to_dict('records'),
            page_size=10),


        html.Div(id='app-2-display-value'),
        dcc.Link('Go to dash 1 - map', href='/dash1'),
        html.Div(),
        dcc.Link('Return Home', href='/'),
    ]
)

from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table

from app import app
import geopandas as gpd
hospitals = gpd.read_file('https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0.geojson')
hospitals = hospitals.drop('geometry',axis=1)

layout = html.Div(
    [
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

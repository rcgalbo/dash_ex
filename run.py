import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import Flask

server = Flask("my app")

app2 = dash.Dash(name='place1', sharing=True, server=server, url_base_pathname='/test1/')

app2.layout = html.Div([
        html.H1('This is a test1')
    ])

app3 = dash.Dash(name='place2', sharing=True, server=server, url_base_pathname='/test2/')

app3.layout = html.Div([
        html.H1('This is test2')
    ])

server.run(port=80, host='0.0.0.0')
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd


PAGE_SIZE = 5


app = dash.Dash(name='tabel2', sharing=True, server=server, url_base_pathname='/table2/')


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df[' index'] = range(1, len(df) + 1)


app.layout = dash_table.DataTable(
    id='datatable-paging',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],
    pagination_settings={
        'current_page': 0,
        'page_size': PAGE_SIZE
    },
    pagination_mode='be'
)


@app.callback(
    Output('datatable-paging', 'data'),
    [Input('datatable-paging', 'pagination_settings')])
def update_graph(pagination_settings):
    return df.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
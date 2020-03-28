import dash
import os

from flask import send_from_directory

import geopandas as gpd
import folium
hospitals = gpd.read_file('https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0.geojson')
hospitals = hospitals.drop('geometry',axis=1)

#create map
folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=3,
                        tiles="CartoDB dark_matter")

for data in zip(hospitals.LATITUDE,hospitals.LONGITUDE):
  marker = folium.CircleMarker(location=(data[0],data[1]),radius=1)
  marker.add_to(folium_map)
folium_map.save(os.getcwd()+'/assets/hospital_map.html')


# read data
app = dash.Dash(__name__)
server = app.server
app.config['suppress_callback_exceptions']=True
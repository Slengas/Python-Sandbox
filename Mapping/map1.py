import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
map_style = "Stamen Terrain"

file_save_loc = "Map1.html"
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 2000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[40.582011, -118.233058],
                 zoom_start=5, tiles=map_style)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(
        iframe), color='gray', fill=True, fill_opacity=0.85, fill_color=color_producer(el)))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10_000_000 else 'orange' if 10_000_000 <= x['properties']['POP2005'] < 50_000_000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save(file_save_loc, close_file=True)

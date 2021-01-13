import folium
import pandas
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

def get_color(elev):
    if 0 < elev <= 2000:
        return "green"
    elif  2000 < elev <= 3000:
        return "orange"
    else:
        return "red"

markers = folium.FeatureGroup(name="Volcanoes in USA")
polygons = folium.FeatureGroup(name="Population according to 2005 Census")

data = pandas.read_csv("Volcanoes.txt")

for lat, long, name, location, elev in zip(data["LAT"], data["LON"], data["NAME"], data["LOCATION"], data["ELEV"]):
    markers.add_child(folium.CircleMarker(location=[lat, long], tooltip = "%s, %s" %(name, location),radius=6, fill_color=get_color(elev), color="black", fill_opacity=0.7))
polygons.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 25000000
else 'orange' if 25000000 <= x['properties']['POP2005']  < 50000000 else 'red'}))
map.add_child(markers)
map.add_child(polygons)
map.add_child(folium.LayerControl())
map.save("Map.html")
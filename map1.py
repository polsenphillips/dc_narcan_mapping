import folium
import pandas as pd

df = pd.read_excel('narcan_addresses.xlsx')
coordinates = df['latlong'] 

map = folium.Map(location = [38.871535322579625, -77.09971749509793], zoom_start = 14, tiles = 'Stamen Terrain')
fg = folium.FeatureGroup(name = 'My Map')

for coordinate in coordinates:
    fg.add_child(folium.Marker(location=coordinates, icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save('Map1.html')
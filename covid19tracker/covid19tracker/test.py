import folium
map_osm = folium.Map(location=[45.5236, -122.6750])
print(map_osm)
map_osm.save('index.html')
# map_osm.create_map(path='osm.html')
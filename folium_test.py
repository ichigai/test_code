import folium


m = folium.Map(location=(35.03708635608637, 136.81576114249268))

folium.Marker(
    location=[34.863714237094094, 136.8123648732452],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)
m.save("folium_test.html")
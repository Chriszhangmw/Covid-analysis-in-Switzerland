

import pandas as pd
us_cities = pd.read_csv("map.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Inflection"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=500)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# import pandas as pd
# us_cities = pd.read_csv("map.csv")
#
# import plotly.express as px
#
# fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Inflection"],
#                         color_discrete_sequence=["fuchsia"], zoom=3, height=500)
# fig.update_layout(
#     mapbox_style="white-bg",
#     mapbox_layers=[
#         {
#             "below": 'traces',
#             "sourcetype": "raster",
#             "source": [
#                 "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
#             ]
#         }
#       ])
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()











token = 'pk.eyJ1IjoibWVpd2VpemhhbmciLCJhIjoiY2s4aHRlYnY0MDFwMzNmbjd4ZDduNjcwbiJ9.rN1JogPjCZwKKR58HL1FhA' # you will need your own token
import pandas as pd
us_cities = pd.read_csv("map.csv")
import plotly.express as px
fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Inflection"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=500)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
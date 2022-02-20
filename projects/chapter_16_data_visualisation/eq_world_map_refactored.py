import json

from matplotlib.font_manager import json_dump
from matplotlib.pyplot import title
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data
file_path = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/'
#file_name = file_path + 'eq_data_30_day_m1.json'
#file_name = file_path + 'eq_data_1_day_m1.json'
file_name = file_path + 'eq_data_7_day_m1.json'

with open(file_name) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])



# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]


my_layout = Layout(title=title)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')


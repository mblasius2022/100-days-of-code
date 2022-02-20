import csv

from datetime import datetime
from matplotlib.pyplot import title
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data
file_path = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/'
file_name = file_path + 'world_fires_1_day.csv'

number_of_rows = 1000

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get brightnesses, lats and lons, and dates.
    dates, brightnesses = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)

        row_num += 1

        if row_num == number_of_rows:
            break


# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
    
}]


my_layout = Layout(title='Global Fires')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='global_fires.html')


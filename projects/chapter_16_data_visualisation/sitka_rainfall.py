import csv
import matplotlib.pyplot as plt
from datetime import datetime

from numpy import tile

file_path = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/'
file_name = file_path + 'sitka_weather_2018_simple.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, header in enumerate(header_row):
        print(f"{index} {header}")
    

    # get dates and high temps
    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        try:
            rainfall = int(row[5])
            
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            rainfalls.append(rainfall)

    # plot the rainfall
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfalls, c='red', alpha=0.5)

    #format plot
    title = ("Daily rainfall Sitka, 2018")
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rain (Inches)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
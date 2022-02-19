import csv
from fileinput import filename
from shutil import which

import matplotlib.pyplot as plt
from numpy import size

from datetime import datetime


#filename = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/sitka_weather_07-2018_simple.csv'
filename = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temps
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
    
    # plot the high temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='blue')

    #format plot
    ax.set_title("Daily high temperatures, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temp(F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
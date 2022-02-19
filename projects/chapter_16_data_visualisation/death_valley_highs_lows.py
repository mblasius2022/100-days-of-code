import csv
import matplotlib.pyplot as plt
from datetime import datetime
from numpy import tile

#filename = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/sitka_weather_07-2018_simple.csv'
file_path = '/home/marioblasius/git/100-days-of-code/projects/chapter_16_data_visualisation/data/'
file_name = file_path + 'death_valley_2018_simple.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temps
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
    # plot the high temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


    #format plot
    title = ("Daily temperatures, 2018\nDeath Valley, CA")
    ax.set_title(title, fontsize=20)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temp(F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
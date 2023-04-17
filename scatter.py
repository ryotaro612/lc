import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def time_to_min(time):
    h, m,s = time.split(':')
    return (int(h) * 3600 + int(m) * 60 + int(s)) / 60

def handle(difficulty):
    with open('./sessions.csv') as f:
        x, y, attempts = [], [], []
        for record in [r for r in csv.DictReader(f) if r['Difficulty'] == difficulty]:
            date = datetime.datetime.strptime(record['Date'], '%Y-%m-%d')
            time_min = time_to_min(record['Time'])
            attempts.append(int(record['# of unsuccessful attempts']))
            x.append(date)
            y.append(time_min)
        mx_attempts = max(attempts)
    plt.scatter(x, y, c=[a/mx_attempts for a in attempts], cmap='coolwarm')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.title('Medium difficulty problems session')
    plt.xlabel('Date')
    plt.ylabel('Elapsed time (min)')
    plt.savefig(filename := f'./{difficulty.lower()}.png')
    return filename
    

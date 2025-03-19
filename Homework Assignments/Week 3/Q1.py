# ⁠Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.
import pandas as pd

import matplotlib.pyplot as plt

# Read the dataset

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"

df = pd.read_csv(url)

day=pd.to_datetime(df['hour_beginning']).dt.day_name()
c={'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0}

for i in range(len(day)):
    if day[i] in c.keys():
        c[day[i]]+=1

plt.plot(c.keys(), c.values(), marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.title('Pedestrian Count for Each Day of the Week')
plt.show()
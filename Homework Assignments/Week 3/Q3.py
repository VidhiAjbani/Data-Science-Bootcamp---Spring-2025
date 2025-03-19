'''⁠Implement a custom function to categorize time of day into morning, afternoon, evening, and night, 
and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian 
activity patterns throughout the day.'''

import pandas as pd
import matplotlib.pyplot as plt

def categorize_time(h):
    if 4<h<11:
        return 'Morning'
    elif 11<h<16:
        return 'Afternoon'
    elif 16<h<21:
        return 'Evening'
    else:
        return 'Night'

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
df['hour_beginning']=pd.to_datetime(df['hour_beginning'])

df['Time of the Day']=df['hour_beginning'].dt.hour.apply(categorize_time)

pedestrian_activity=df['Time of the Day'].value_counts().to_dict()
desired_order=['Morning','Afternoon','Evening','Night']
rearranged_dict={key:pedestrian_activity[key] for key in desired_order}

plt.bar(rearranged_dict.keys(),rearranged_dict.values())
plt.xlabel('Time of the Day')
plt.ylabel('Pedestrian Activity')
plt.title('Pedestrian Activity throughout the Day')
plt.show()





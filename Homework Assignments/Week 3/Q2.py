'''Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity 
in that year. Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix) between weather 
patterns and pedestrian counts for the selected year.'''

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"

df = pd.read_csv(url)

df_2019=df[pd.to_datetime(df['hour_beginning']).dt.year==2019]
new_df=df_2019[df_2019['location']=='Brooklyn Bridge'][['weather_summary','Pedestrians']]
df_pandas_encoded = pd.get_dummies(new_df, columns=['weather_summary'], drop_first=True)
#counts=new_df.groupby('weather_summary')['Pedestrians'].count()
cor=df_pandas_encoded.corr()

plt.figure(figsize=(12, 6))
sns.heatmap(cor, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation between Weather and Pedestrian Counts on Brooklyn Bridge (2019)')
plt.show()
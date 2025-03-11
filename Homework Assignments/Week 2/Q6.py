# Q-6) Replace missing values in Min.Price and Max.Price columns with their respective mean.

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print("Before Changes:")
print("Number of missing values in Min.Price: ",df['Min.Price'].isnull().sum())
print("Number of missing values in Max.Price: ",df['Max.Price'].isnull().sum())

df['Min.Price']=df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price']=df['Max.Price'].fillna(df['Max.Price'].mean())

print("After Changes:")
print("Number of missing values in Min.Price: ",df['Min.Price'].isnull().sum())
print("Number of missing values in Max.Price: ",df['Max.Price'].isnull().sum())
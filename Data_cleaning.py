import csv 
import pandas as pd


df = pd.read_csv('Data_clean.csv')

print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

print(df.shape)


df = df.rename({
    'Star_name.1': "Star_name",
    'Distance.1': "Distance",
    'Mass.1': "Mass",
    'Radius.1': "Radius"
    }, axis = 'columns')


df.to_csv('final.csv')
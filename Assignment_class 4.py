from pandas import Series, DataFrame
import pandas as pd
import numpy as np
main_dir = "/Users/robin/Desktop/Big Data/Data"
git_dir = "/Users/robin/Desktop/Big Data/GitHub"
csv_file = "/small_data_w_missing_duplicated.csv"
df = pd.read_csv(main_dir + csv_file)
df.head(10)
df.tail(10)
missing = [".", "NA", "NULL", " ", "-"]
df = pd.read_csv((main_dir + csv_file), na_values = missing)
df.head(10)
df.drop_duplicates(['panid', 'date', 'consump'])
df.drop_duplicates(['consump'])
df['consump'].isnull()
rows = df['consump'].isnull()
df[rows]
df.dropna(subset=['consump'])
df['consump'].isnull()
df.dropna(subset=['consump'])
df[rows]
rows = df2['consump'].isnull()
df2[rows]
dupvalues = df.duplicated(subset = ['panid', 'date'])
df[dupvalues]
dupvalues.dropna(subset=['consump'])
df4 = df[dupvalues]
df4
df5 = df4.dropna(axis = 0, how = 'any')
df5
df5['consump'].mean()
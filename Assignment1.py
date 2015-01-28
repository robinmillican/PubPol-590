import pandas as pd
import numpy as np
from pandas import Series, DataFrame
## assigning file paths
main_dir = "/Users/robin/Desktop/Big Data/GitHub/PubPol-590"
csv_file = "/data/sample_data_clean.csv"
txt_file = "/data/sample_data_clean.txt.html"

main_dir + csv_file
## read_csv and read_table
pd.read_csv(main_dir + csv_file)
df = pd.read_csv(main_dir + csv_file)
df[60:99]
df.consump[<0.3]
c = df.consump
df[df.consump > 0.3]
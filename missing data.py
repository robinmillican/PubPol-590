from pandas import Series, DataFrame
import pandas as pd
import numpy as np
main_dir = "/Users/robin/Desktop/Big Data/Data"
git_dir = "/Users/robin/Desktop/Big Data/GitHub"
csv_file = "/sample_missing.csv"
df = pd.read_csv(main_dir + csv_file)
df
df.head() # gives top 5 rows by default
df.head(10) # head(n) gives top (n) rows
df[:10] #slicing - same thing
df.tail(10) #tail(n) gives bottom (n) rows
df['consump'].head(10).apply(type) # apply function 'type' to top 10 rows 
#in 'consump' column

## we don't want String Data. Periods common placeholders for missing data
#in some programming languages (STATA), so we need to create new missing value 
# sentinals (substitutes for missing values)
missing = [".", "NA", "NULL", " "] ##defining missing values for iPython to
#look for
df = pd.read_csv((main_dir + csv_file), na_values = missing) ## allows us to
#define what symbols should be interpreted as missing
df.head(10)
df['consump'].head(10).apply(type) 
## MISSING DATA (USING SMALLER DATAFRAMES)
[1,2,3]*3 #repeating lists by multiplying
## types of missing data are none and np.nan
none
np.nan
type(none)
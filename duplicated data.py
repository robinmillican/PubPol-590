from pandas import Series, DataFrame
import pandas as pd
import numpy as np
##creating a new dataframe
zip3= zip(['red','green','blue', 'orange']*4,['5','10','20','40']*3,[':(',':D',':D']*4)
df3 = DataFrame(zip3, columns = ['A','B','C'])
df3
##  pandas method 'duplicated' 
df3.duplicated() #searching DF from top to bottom by default, uses values 
#in entire row -- tags duplicates as 'true'
df3.duplicated(take_last =True) #searches bottom to top

## subset duplicated values
df3.duplicated(subset =['A','B']) ##omitting column 'C' for duplicate search
df3.duplicated(['A','B'])

##HOW TO GET ALL VALUES THAT HAVE DUPLICATES (not keeping the original value)
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t)
unique = ~t_b & ~b_t
unique
df3[unique]

#dropping duplicates
df3.drop_duplicates()
df3.drop_duplicates(take_last = True)

#different way to do same thing
t_b = df3.duplicated()
df3[~t_b]

#subset criteria
df3.drop_duplicates() == df3[~t_b]
df3.drop_duplicates(['A', 'B'])

## if you want to keep the first duplicated value (from top) and remove others
df3.drop_duplicates()

## same, but from the bottom
df3.drop_duplicates(take_last = True)
## purge all values that are duplicates
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # complement where either is true
df3[unique]
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/robin/Desktop/Big Data/Data"
git_dir = "/Users/robin/Desktop/Data for PUBPOL590/"
csv_file = "sample_data_clean.csv"
df = pd.read.csv(os.path.join(main_dir, csv_file))
str1 = "Hello, Computer"
str2 = "Hello, Human"
str3 = u'eep'

type(str1) # type str
type(str2) #type str
type (str3) #type unicode

##numeric
int1 = 10
float1 = 20.56
long1 = 999999999999999999999999999999

## logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)

#CREATING LISTS AND TUPLES
## in brief, lists can be changed, tuples cannot
## we almost exclusively use lists
list1 = []
list2 = [1,2,3]
list2[2] #output 3
list2[2] = 5

## tuples, can't change
tup1 = (8,3,19)
tup1[2] # of outputs is 19
tup1[2] = 5

## convert
list2 = list(tup1)
tup2 = tuple(list1)

## lists can be appended and extended
list2.append([3,90]) # out: [8,3,19,[3,90]}
list3 = [8,3, 19]
list3.extend ([6,88]) # out: [8, 3, 19, 6, 88]
len(list3)

#CONVERTING LISTS TO SERIES AND DATAFRAME
list4 = range(5,10) # range(n,m) -- gives list from #n to m-1
list4 #out : [5,6,7,8,9]
list5 = range (5) 
list5 #out: [0,1,2,3,4]
list6 = ['q', 'r', 's', 't', 'u']

##list to series
s1 = Series(list4)
s2 = Series(list6)

## create dataframe from lists OR series
list7 = range(60, 65)
zip(list4, list6)
zip1 = zip(list4, list6, list7)
df1 = DataFrame(zip1)
df2 = DataFrame(zip1, columns = ['two', 'apple', ':)'])
df2 = DataFrame(zip1, columns = [2, '2', ':)']) 
df2[2] # reference column with key (int) 2
df2['2'] # reference column with key (str) '2'
df2[3:4] # slice out row 3
df2[['2',':)']][3:4] # to get column '2' and ';)' then get row 3
##make dataframe using dict notation
df4 = DataFrame({ ':(' : list4, 7: list6})
dict1 = { ':(' : list4, 9: list6}


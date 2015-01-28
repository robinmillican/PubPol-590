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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/stable/io.html

# data
#date,A,B,C
#20090101,a,1,2
#20090102,b,3,4
#20090103,c,4,5


# Imports
import pandas as pd
import StringIO

df = pd.read_csv('foo.csv')
print("\n df")

print(df)

# In the case of indexed data, you can pass the column number or
# column name you wish to use as the index:
print("\n index_col = 0")
df =  pd.read_csv('foo.csv', index_col=0)
print(df)

print("\n index_col = date")
pd.read_csv('foo.csv', index_col='date')
print(df)


# You can also use a list of columns to create a hierarchical index:
print("\nindex_col=[0, 'A']")
df =  pd.read_csv('foo.csv', index_col=[0, 'A'])
print(df)

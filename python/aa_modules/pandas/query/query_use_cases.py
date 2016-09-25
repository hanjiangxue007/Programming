#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# A use case for query() is when you have a collection of DataFrame objects
# that have a subset of column names (or index levels/names) in common.
# You can pass the same query to both frames without having to specify which
# frame you’re interested in querying

n = 10
df = pd.DataFrame(np.random.rand(n,3), columns=list('abc'))
print("\n")
print(df)

df2 = pd.DataFrame(  np.random.rand(n+2, 3), columns= df.columns  )
print("\n")
print(df2)


expr = '0.0 <= a <= c <= 0.5'
df3 = map( lambda frame: frame.query(expr),  [df,df2]  )
print("\n")
print(df3)

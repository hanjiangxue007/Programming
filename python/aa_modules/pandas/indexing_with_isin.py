#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print("\n")
print(s)


print("\n")
print( s.isin([2, 4, 6])   )


print("\n")
print( s[s.isin([2, 4, 6])]   )


# The same method is available for Index objects and is useful for the cases
# when you don’t know which of the sought labels are in fact present:

print("\n")
print( s[s.index.isin([2, 4, 6])]  )


# compare it to the following
print("\n")
print(   s[[2, 4, 6]]  )


##=============================================================================
df = pd.DataFrame({'vals': [1, 2, 3, 4],
                   'ids' : ['a', 'b', 'f', 'n'],
                   'ids2': ['a', 'n', 'c', 'n']})

print("\n")
print(df)
values = ['a', 'b', 1, 3]
print("\n")
print(  df[  df.isin(values)  ]  )


# Oftentimes you’ll want to match certain values with certain columns.
# Just make values a dict where the key is the column, and the value is a
# list of items you want to check for.

values = {'ids': ['a', 'b'], 'vals': [1, 3]}
print("\n")
print(  df[   df.isin(values)   ])


# Combine DataFrame’s isin with the any() and all() methods to quickly select
# subsets of your data that meet a given criteria. To select a row where each
# column meets its own criterion:
print("\n")
print(df)
values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}

row_mask = df.isin(values).all(1)
print("\n")
print(  df[row_mask]  )

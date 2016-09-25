#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fast scalar value getting and setting using at
# If you only want to access a scalar value, the fastest way is to use the at
# and iat methods, which are implemented on all of the data structures.

# Similarly to loc, at provides label based scalar lookups, while, iat provides
# integer based lookups analogously to iloc

s = pd.Series(np.arange(6))
print(s)

print("\n")
print(s.iat[5])




dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print("\n")
print(df)

print("\n")
print(df.at[dates[5], 'A'])
print(df.iat[5, 0])

# set new value
df.at[dates[5], 'A'] = 7
df.iat[5, 0] = 70
print(df.iat[5, 0])

# at may enlarge the object in-place as above if the indexer is missing.
print("\n")
print(df)
df.at[dates[-1]+1, 0] = 7
print("\n")
print(df)

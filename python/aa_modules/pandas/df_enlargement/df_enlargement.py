#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# series
s = pd.Series([1,2,3])
s[5] = 5.  # add a value
print(s)


# DataFrame
print("\n")
df = pd.DataFrame(np.arange(6).reshape(3,2),
                    columns=['A','B'])

print(df)

# A DataFrame can be enlarged on either axis via .loc
df.loc[:,'C'] = df.loc[:,'A']*2

print("\n")
print(df)


# This is like an append operation on the DataFrame.
df.loc[3] = 500  # all third row values
print("\n")
print(df)

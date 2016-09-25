#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Note While standard Python / Numpy expressions for selecting and setting
# are intuitive and come in handy for interactive work, for production code,
# we recommend the optimized pandas data access methods,
# .at, .iat, .loc, .iloc and .ix.
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print(df.loc[dates[0]])
print(df.loc[:,['A','B']])

# Showing label slicing, both endpoints are included
print(df.loc['20130102':'20130104',['A','B']])


# Reduction in the dimensions of the returned object
print("\n")
print(df.loc['20130102',['A','B']])

# For getting a scalar value
print("\n")
print(df.loc[dates[0],'A']) # 0th value of A

# For getting fast access to a scalar (equiv to the prior method)
print("\n")
print(df.at[dates[0],'A'])  # 0th value of A

# Select via the position of the passed integers
print("\n")
print(df.head())
print(df.iloc[3]) # 4th index or, row value

# By integer slices, acting similar to numpy/python
print("\n")
print(df.iloc[3:5,0:2])

# By lists of integer position locations, similar to the numpy/python style
print("\n")
print(df.iloc[[1,2,4],[0,2]])

# For slicing rows explicitly
print("\n")
print(df.iloc[1:3,:])

# For slicing columns explicitly
print("\n")
print(df.iloc[:,1:3])


# For getting a value explicitly
print("\n")
print(df)
print(df.iloc[1,1])

# For getting fast access to a scalar (equiv to the prior method)
print("\n")
print(df.iat[1,1])















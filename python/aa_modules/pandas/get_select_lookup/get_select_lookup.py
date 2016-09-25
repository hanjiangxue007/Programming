#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==============================================================================
# Dictionary-like get() method

# Each of Series, DataFrame, and Panel have a get method which can return a default value.

s = pd.Series([1,2,3], index=['a','b','c'])

s1 = s.get('a')               # equivalent to s['a']
print("\n")
print(r"s.get('a')")
print(r"equivalent to s['a']")
print("\n")
print(s)
print("\n")
print(s1)


s1 = s.get('x', default=-1)               # equivalent to s['a']
print("\n")
print(r"s.get('x', default=-1)")
print("\n")
print(s)
print("\n")
print(s1)

#==============================================================================
# The select() Method

# Another way to extract slices from an object is with the select method of
# Series, DataFrame, and Panel. This method should be used only when there is
# no more direct way. select takes a function which operates on labels along axis
# and returns a boolean. For instance:

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df1 = df.select(lambda x: x== 'A', axis=1)
print(df)
print("\n")
print(df1)


#==============================================================================
# The lookup() Method

# Sometimes you want to extract a set of values given a sequence of row labels
# and column labels, and the lookup method allows for this and returns a numpy array.

df = pd.DataFrame(np.random.rand(20,4), columns = ['A','B','C','D'])
df2 = df.lookup(list(range(0,10,2)), ['B','C','A','B','D'])

print("\n")
print(df)
print("\n")
print(df2)
print(['B','C','A','B','D'])
print(list(range(0,10,2)))

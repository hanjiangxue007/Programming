#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Note      : pure python is faster below 50,000 rows.
# Note      : query       is faster above 200, 000 rows

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print("\n")
print(df)


# pure python
df1 = df[(df.a < df.b) & (df.b < df.c)]
print("\n")
print(df1)

# query
df1 = df.query('(a < b) & (b < c)')
print("\n")
print(df1)


df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
df.index.name = 'a'
print("\n")
print(df)

df1 = df.query('a < b and b < c')
print("\n")
print(df1)

df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
df.index.name = 'a'
print("\n")
print(df)


# If instead you don’t want to or cannot name your index, you can use the name
# index in your query expression:

df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))
print("\n")
print(df)

df1 = df.query('index < b < c')
print("\n")
print(df1)

# Note

# If the name of your index overlaps with a column name, the column name is
# given precedence. For example,

df = pd.DataFrame({'a': np.random.randint(5, size=5)})
df.index.name = 'a'

df1 = df.query('a > 2') # uses the column 'a', not the index
print("\n")
print(df1)

# You can still use the index in a query expression by using the
# special identifier ‘index’:

df1 = df.query('index > 2')
print("\n")
print(df1)

# If for some reason you have a column named index, then you can refer to the
# index as ilevel_0 as well, but at this point you should consider renaming
# your columns to something less ambiguous.

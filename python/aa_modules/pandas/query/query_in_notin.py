#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : June 15, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# query() also supports special use of Python’s in and not in comparison operators,
# providing a succinct syntax for calling the isin method of a Series or DataFrame.

# get all rows where columns "a" and "b" have overlapping values
df = pd.DataFrame({ 'a': list('aabbccddeeff'),
                    'b': list('aaaabbbbcccc'),
                    'c': np.random.randint(5, size=12),
                    'd': np.random.randint(9, size=12)  })


print("\n")
print(df)


df1 = df.query('a in b')
print("\n")
print(df1)

# How you'd do it in pure Python
df1 = df[df.a.isin(df.b)]
print("\n")
print(df1)


df1 = df.query('a not in b')
print("\n")
print(df1)

# How you'd do it in pure Python
df1 = df[~df.a.isin(df.b)]
print("\n")
print(df1)


# You can combine this with other expressions for very succinct queries:

# rows where cols a and b have overlapping values and col c's values are less than col d's
df1 = df.query('a in b and c < d')
print("\n")
print(df1)

# pure Python
df1 = df[df.a.isin(df.b) & (df.c < df.d)]
print("\n")
print(df1)

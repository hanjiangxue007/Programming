#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : June 15, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# query() Python versus pandas Syntax Comparison
n = 10
df = pd.DataFrame( np.random.randint(n, size=(n,3)) , columns=list('abc'))
print("\n")
print(df)


df1 = df.query('  (a<b) & (b<c)     ')
print("\n")
print(df1)


# Slightly nicer by removing the parentheses (by binding making comparison operators bind tighter than &/|)

df1 = df.query(' a<b & b<c    ')
print("\n")
print(df1)

# Use English instead of symbols
df1 = df.query(' a<b and b<c    ')
print("\n")
print(df1)


# Pretty close to how you might write it on paper
df1 = df.query(' a<b<c   ')
print("\n")
print(df1)

#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : June 15, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# You can negate boolean expressions with the word not or the ~ operator.
n = 10
df = pd.DataFrame(np.random.rand(n,3), columns=list('abc'))



print("\n")
print(df)


df['bools'] = np.random.rand(len(df)) > 0.5
print("\n")
print(df)


df1 = df.query('  ~bools   ') # df.query(' not bools ')
print("\n")
print(df1)


df1 = df.query(' not bools   ') == df[ ~df.bools  ]
print("\n")
print(df1)

#==============================================================================
# short query syntax
shorter = df.query('a < b < c and (not bools) or bools > 2')
print("\nshorter\n")
print(shorter)

# equivalent in pure Python
longer = df[(df.a < df.b) & (df.b < df.c) & (~df.bools) | (df.bools > 2)]
print("\nlonger\n")
print(longer)


mylogic = shorter == longer
print("\n")
print(mylogic)

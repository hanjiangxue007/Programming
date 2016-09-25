#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced 


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Special use of the == operator with list objects
# Comparing a list of values to a column using ==/!= works similarly to in/not in


# get all rows where columns "a" and "b" have overlapping values
df = pd.DataFrame({ 'a': list('aabbccddeeff'),
                    'b': list('aaaabbbbcccc'),
                    'c': np.random.randint(5, size=12),
                    'd': np.random.randint(9, size=12)  })


print("\n")
print(df)

#==============================================================================

df1 = df.query(' b == ["a", "b"]    ')
print("\n")
print(df1)


# Pure Python
df1 = df[  df.b.isin( ["a", "b"] )   ]
print("\n")
print(df1)


df1 = df.query('  c == [1,2]   ')
print("\n")
print(df1)

df1 = df[  df.c.isin([1,2])   ]
print("\n")
print(df1)
#==============================================================================
# using in/not in
df1 =  df.query('[1, 2] in c')
print("\nusing in/not in\n")
print(df1)

# values not in the list
df1 = df.query('  c != [1,2]   ')
print("\n")
print(df1)

df1 = df.query('  [1,2] not in c     ')
print("\n")
print(df1)



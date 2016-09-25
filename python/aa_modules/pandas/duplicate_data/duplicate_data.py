#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#  If you want to identify and remove duplicate rows in a DataFrame, there are
#  two methods that will help: duplicated and drop_duplicates. Each takes as an
#  argument the columns to use to identify duplicated rows.

#  duplicated returns a boolean vector whose length is the number of rows,
#  and which indicates whether a row is duplicated.
#  drop_duplicates removes duplicate rows.

#  By default, the first observed row of a duplicate set is considered unique,
#  but each method has a keep parameter to specify targets to be kept.

#  keep='first' (default): mark / drop duplicates except for the first occurrence.
#  keep='last': mark / drop duplicates except for the last occurrence.
#  keep=False: mark / drop all duplicates.

df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
                    'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
                    'c': np.random.randn(7)})



print("\n")
print(df2)

logic1 = df2.duplicated('a') # looks duplicates from first row of column a
print("\nduplicated is logic and duplicates is dataframe")
print(logic1)


logic1 = df2.duplicated('a', keep='last') # looks duplicates from last row of column a
print("\n")
print(df2)
print("\n")
print(logic1)


logic1 = df2.duplicated('a', keep=False) # only duplicated items are True
print("\nkeep = False\n")
print(df2)
print("\n")
print(logic1)


df3 = df2.drop_duplicates('a', keep='last')
print("\nkeep = last\n")
print(df2)
print("\n")
print(df3)


df3 = df2.drop_duplicates('a', keep=False)
print("\n")
print(df2)
print("\n")
print(df3)
#==============================================================================
# Also, you can pass a list of columns to identify duplications.

logic1 = df2.duplicated( ['a','b'])
print("\nduplicated logic columns a b\n")
print(df2)
print("\n")
print(logic1)

df3 = df2.drop_duplicates( [ 'a', 'b']   )
print("\ndrop_duplicates columns a b")
print(df2)
print("\n")
print(df3)

#==============================================================================
# To drop duplicates by index value, use Index.duplicated then perform slicing.
# Same options are available in keep parameter.

df3 = pd.DataFrame({'a': np.arange(6),
                    'b': np.random.randn(6)},
                    index=['a', 'a', 'b', 'c', 'b', 'a'])

print("\ndrop duplicates by index value\n")
print(df3)

logic1 = df3.index.duplicated()
print("\ndf3.index.duplicated\n")
print(logic1)

# first duplicated items
df4 = df3[ ~df3.index.duplicated()  ]
print("\n")
print(r"df3[ ~df3.index.duplicated()")
print(df3)
print("\n")
print(df4)

# last duplicated items
df4 = df3[~df3.index.duplicated(keep='last')]
print("\n")
print(r"df3[~df3.index.duplicated(keep='last')]")
print(df3)
print("\n")
print(df4)


# only not duplicated items
df4 = df3[~df3.index.duplicated(keep=False)]
print("\n")
print(r"df3[~df3.index.duplicated(keep=False)]")
print(df3)
print("\n")
print(df4)



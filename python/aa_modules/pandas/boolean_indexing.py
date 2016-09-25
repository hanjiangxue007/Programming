#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(range(-3, 4))
print(s)



print("\n")
print(s[s > 0])


print("\n")
print(s[(s < -1) | (s > 0.5)])


print("\n")
print(  s[~(s < 0)]  )



# dataframe
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("\n")
print(df)


# You may select rows from a DataFrame using a boolean vector the same length
# as the DataFrame’s index (for example, something derived from one of the
# columns of the DataFrame):

print("\n")
print(df[df['A'] > 0])

# List comprehensions and map method of Series can also be used to produce more complex criteria:
df2 = pd.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                    'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                    'c' : np.random.randn(7)})

# only want 'two' or 'three'
criterion = df2['a'].map(lambda x: x.startswith('t'))
print(df2[criterion])

# equivalent but slower
print("\n")
print(  df2[[x.startswith('t') for x in df2['a']]]  )


# Multiple criteria
print("\n")
print(  df2[criterion & (df2['b'] == 'x')]  )

# Note, with the choice methods Selection by Label, Selection by Position,
# and Advanced Indexing you may select along more than one axis using boolean
# vectors combined with other indexing expressions.
print("\n")
print(  df2.loc[criterion & (df2['b'] == 'x'),'b':'c'] )

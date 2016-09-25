#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print("\n")
print(s)

print("\n")
print(s[s > 0])


# To return a Series of the same shape as the original
print("\n")
print(s.where(s > 0))




##=============================================================================
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df = pd.DataFrame(np.linspace(-10,13,num=24).reshape(6,4), index=dates, columns=list('ABCD'))

print("\n")
print(df)


print("\n")
print(df[df < 0])


# In addition, where takes an optional other argument for replacement of
# values where the condition is False, in the returned copy.

df2 = df.where(df < 0, -df)
df2 = df.where(df < 0, -999)
print("\n")
print(df2)


# By default, where returns a modified copy of the data.
# There is an optional parameter inplace so that the original data can be
# modified without creating a copy:

df_orig = df.copy()

df_orig.where(df > 0, -999, inplace=True);

print("\n")
print( df_orig)



# alignment
# Furthermore, where aligns the input boolean condition (ndarray or DataFrame),
# such that partial selection with setting is possible. This is analogous to
# partial setting via .ix (but on the contents rather than the axis labels)

df2 = df.copy()
print("\n")
print(df2)

df2[ df2[1:4] > 0 ] = 999

print("\n")
print(df2)


# Where can also accept axis and level parameters to align the input when performing the where.

df2 = df.copy()

df3 = df2.where(df2>0,df2['A'],axis='index')
print("\n")
print(df3)

# This is equivalent (but faster than) the following.
df2 = df.copy()
df3 = df.apply(lambda x, y: x.where(x>0,y), y=df['A'])
print("\n")
print(df3)


# Where can accept a callable as condition and other arguments. The function
# must be with one argument (the calling Series or DataFrame) and that returns
# valid output as condition and other argument.

df3 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]})

print("\n")
print(df3)
print(pd.__version__)
df4 = df3.where(lambda x: x > 4, lambda x: x + 10)
print("\n")
print(df4)


##=============================================================================
# mask

# mask is the inverse boolean operation of where.
print("\n")
print(s)
print("\n")
print(  s.mask(s >= 0) )

print("\n")
print(df)
print("\n")
print(df.mask(df >= 0))





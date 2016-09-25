#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1,3,5,np.nan,6,8])
print('{} {} {}'.format('\ns = \n', s, ''))



# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101',periods=6)
print('{} {} {}'.format('\ndates:\n', dates, ''))


df = pd.DataFrame(np.random.randn(6,4),
                  index = dates,
                  columns = list('ABCD'))
print('{} {} {}'.format('\ndf:\n', df, ''))



# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4 ,dtype='int32'),
                     'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                     'F' : 'foo'
                   })

print('{} {} {}'.format('\ndf2:\n', df2, ''))
print('{} {} {}'.format('\ndf2.dtypes\n', df2.dtypes, ''))


# NOTE: for IPython, df2.<TAB> shows subset of attributes



##=============================================================================
# Viewing Data
print('{} {} {}'.format('\ndf.head(3)\n', df.head(3), ''))
print('{} {} {}'.format('\ndf.tail(3)\n', df.tail(3), ''))


# Display the index, columns, and the underlying numpy data
print('{} {} {}'.format('\ndf.index\n', df.index, ''))
print('{} {} {}'.format('\ndf.columns\n', df.columns, ''))
print('{} {} {}'.format('\ndf.values\n', df.values, ''))


# Describe shows a quick statistic summary of your data
print('{} {} {}'.format('\ndf.describe()\n', df.describe, ''))
print('{} {} {}'.format('\ndf.T\n', df.T, '\n'))
print('{} {} {}'.format('df.sort_index(axis=1, ascending=False)\n', df.sort_index(axis=1, ascending=False), '\n'))
print('{} {} {}'.format(r'df.sort_values(by='B')', df.sort_values(by='B'), ''))













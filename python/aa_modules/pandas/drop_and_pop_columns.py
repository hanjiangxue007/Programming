#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
df = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4 ,dtype='int32'),
                     'E' : pd.Categorical(['test', 'train', 'test', 'train']),
                     'F' : 'foo'
                   })

print('{} {} {}'.format('\ndf2:\n', df, ''))


# drop a column from the dataframe
df = df.drop('A', 1)

# There is an optional parameter inplace so that the original
# data can be modified without creating a copy.

# df.drop('column_name', axis=1, inplace=True)
# df.drop(df.columns[[0, 1, ]], axis=1)  # df.columns is zero-based pd.Index
print('{} {} {}'.format('\ndf2:\n', df, ''))


# using column names is better
# It's good practice to always use the [] notation, one reason is
# that attribute notation (df.column_name) does not work for numbered indices:

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
print('{} {} {} {}'.format('\ndf[1] = \n', df[1],'\n',''))
# df.1 doesnot work.


# delete columns
print('{} {} {} {}'.format('\ndeleting columns\n', '','',''))
df = pd.DataFrame.from_items([  ('A', [1, 2, 3]),
				('B', [4, 5, 6]),
                                ('C', [7, 8, 9])    ],
			   orient='index',
			   columns=['one', 'two', 'three'])


print(df)
df.drop(df.columns[[0]], axis=1, inplace=True)
print (df)

# delete column called three
three = df.pop('three')
print (df)

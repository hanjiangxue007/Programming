#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


left_frame = pd.DataFrame({'key': range(5),
                           'left_value': ['a', 'b', 'c', 'd', 'e']})
right_frame = pd.DataFrame({'key': range(2, 7),
                           'right_value': ['f', 'g', 'h', 'i', 'j']})
print(left_frame)
print('\n')
print(right_frame)


#inner join (default)

inner_join = pd.merge(left_frame, right_frame, on='key', how='inner')
print('{} {} {} {}'.format('\n', 'inner_join:\n',inner_join,'\n'))

left_outer_join = pd.merge(left_frame, right_frame, on='key', how='left')
print('{} {} {} {}'.format('\n', 'left_outer_join:\n',left_outer_join,'\n'))


right_outer_join = pd.merge(left_frame, right_frame, on='key', how='right')
print('{} {} {} {}'.format('\n', 'right_outer_join:\n',right_outer_join
,'\n'))

full_outer_join = pd.merge(left_frame, right_frame, on='key', how='outer')
print('{} {} {} {}'.format('\n', 'full_outer_join:\n',full_outer_join,'\n'))


# pandas.concat takes a list of Series or DataFrames and returns a Series
# or DataFrame of the concatenated objects. Note that because the function
# takes list, you can combine many objects at once.

myconcat = pd.concat([left_frame, right_frame])
print('{} {} {} {}'.format('\n', 'concat:\n',myconcat,'\n'))


# By default, the function will vertically append the objects to one another,
# combining columns with the same name. We can see above that values not
# matching up will be NULL.

# Additionally, objects can be concatentated side-by-side using the
# function's axis parameter.

myconcat_axis_1 = pd.concat([left_frame, right_frame], axis=1)
print('{} {} {} {}'.format('\n', 'myconcat_axis_1:\n',myconcat_axis_1,'\n'))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
# https://stackoverflow.com/questions/15891038/pandas-change-data-type-of-columns

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})


# fastest to slowest
print(df.columns.values.tolist())
print(list(df))
print([column for column in df])
print(list(df.columns.values))

# now convert list to DataFrame
mylist = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]
print('{} {} {} {}'.format('\nmylist = \n', mylist,'',''))
df = pd.DataFrame(mylist, columns=['one', 'two', 'three'])
print('{} {} {} {}'.format('\nmylist became df = \n', df,'',''))
print('{} {} {} {}'.format('\ndf.dtypes = \n', df.dtypes,'',''))

# change dtypes
df[['two', 'three']] = df[['two', 'three']].astype(float)
print('{} {} {} {}'.format('\ndf.dtypes = \n', df.dtypes,'',''))

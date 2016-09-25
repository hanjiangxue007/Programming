#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# Using a single column’s values to select data.
print("\n")
print(df[df.A > 0])


# A where operation for getting.
print("\n")
print(df[df > 0])


# Using the isin() method for filtering:
print("\n")
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)
print(df2[df2['E'].isin(['two','four'])])


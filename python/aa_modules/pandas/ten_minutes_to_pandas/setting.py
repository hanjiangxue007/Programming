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

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print("\n")
print(s1)

df['F'] = s1

# Setting values by label
df.at[dates[0],'A'] = 0

# Setting values by position
df.iat[0,1] = 0

# Setting by assigning with a numpy array
df.loc[:,'D'] = np.array([5] * len(df))

# changed result
print("\n")
print(df)

# A where operation with setting.
df2 = df.copy()

df2[df2 > 0] = -df2
print("\n")
print(df2)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),
                  index = dates,
                  columns = list('ABCD'))
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1],'E'] = 1

print(df1)

# To drop any rows that have missing data.
df2 = df1.dropna(how='any')
print(df2)

# Filling missing data

df2 = df1.fillna(value=5)
print(df2)

# To get the boolean mask where values are nan

maskindex = pd.isnull(df1)
print(maskindex)
print(df2[maskindex])



#==============================================================================
print(df)
print(df.apply(np.cumsum))
print(df.A.max(), df.A.min(),df.A.max()-df.A.min())
print(df.apply(lambda x: x.max() - x.min()))

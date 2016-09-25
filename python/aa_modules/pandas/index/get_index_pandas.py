#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : https://stackoverflow.com/questions/18327624/find-elements-index-in-pandas-series 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.DataFrame(np.arange(10).reshape(5,2),columns=['c0','c1'])
print("\n")
print(df)
print("\n")
print('{} {} {}'.format(r'df.ix[0,1] = ',df.ix[0,1], ''))
print('{} {} {}'.format(r'first row, second column = ',df.ix[0,1], ''))

value = 8.0
myindices = df.c0[df.c0 == value].index.tolist()
n = myindices[0]
line = df.iloc[[n]]
print(line)
print('{} {} {}'.format('value = ',value, '\n'))
print('{} {} {}'.format('index of value = ',myindices, '\n'))


##=============================================================================
print('{} {} {}'.format('\n\nexample 2:','', ''))
myseries = pd.Series([1,7,0,7,5], index=['a','b','c','d','e'])
myindices = list(myseries[myseries==7].index)
print('{} {} {}'.format('myindices index= ',myindices, ''))
values_any = (myseries==7).any()
print('{} {} {}'.format('values_any = ',values_any, ''))
myindices = (myseries==7).argmax()
print('{} {} {}'.format('myindices argmax= ',myindices, ''))




##=============================================================================
print('{} {} {}'.format('\n\nexample 3:','', ''))
s = pd.Series([1,3,0,7,5],index=[0,1,2,3,4])
myindices = list(s).index(7) # fastest method
print('{} {} {}'.format('myindices = ',myindices, ''))


##=============================================================================
print('{} {} {}'.format('\n\nexample 4:','', ''))
myseries = pd.Series([1,4,0,7,5], index=[0,1,2,3,4])
myindices = pd.Index(myseries).get_loc(7)
print('{} {} {}'.format('myindices = ',myindices, ''))


##=============================================================================
print('{} {} {}'.format('\n\nexample 5:','', ''))
myseries = pd.Series([1,4,0,7,5], index=[0,1,2,3,4])
myindices = myseries[myseries == 7]
print(myseries)
print('{} {} {}'.format('myindices = ',myindices, ''))

myindices = myseries[myseries == 7].index[0]
print('{} {} {}'.format('\nmyindices = ',myindices, ''))




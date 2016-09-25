#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# create a dataframe
n = 20
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print("\n")
print(df)


# break dataframe
first_ten = pd.DataFrame()
rest = pd.DataFrame()

if df.shape[0] > 10: # len(df) > 10 would also work
    first_ten = df[:10]
    rest = df[10:]


# example 2
first_ten = df.head(10) 
rest      = df.tail( len(df) - 10 )
print("\n")
print(rest)


# exampl 3
df = pd.DataFrame(np.random.randn(105,3))
nrows = 20
frames = [ df.iloc[i*nrows:min((i+1)*nrows,len(df))] for i in xrange(int(len(df)/float(nrows)) + 1) ]

print('{} {} {}'.format('length of frames = ', len(frames), ''))
print("\n")
print(frames[0])
print("\n")
print(frames[len(frames)-1])
print('{} {} {}'.format('length of frames = ', len(frames), ''))


# example 4
df = pd.DataFrame(data=np.random.rand(100, 3), columns=list('ABC'))
groups = df.groupby(np.arange(len(df.index))/10)
for (frameno, frame) in groups:
    frame.to_csv("output_%s.csv" % frameno,index=None, header=None)

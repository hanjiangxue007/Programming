#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# define a dataframe with muliindex
df = pd.DataFrame({('A','a'): [-1,-1,0,10,12],
                   ('A','b'): [0,1,2,3,-1],
                   ('B','a'): [-20,-10,0,10,20],
                   ('B','b'): [-200,-100,0,100,200]})

print('{} {} {}'.format('df = \n', df, ''))



# set subset of A (a,b) values to 0 if they are less than 0
#idx = pd.IndexSlice
#mask = df.loc[:,idx['A',:]]<0
#print('{} {} {}'.format('mast', mask, ''))
#df[mask] = 0
#print(df)

#df[df[['A']]<0] = 0
#print('{} {} {}'.format('df = \n', df, ''))


infile = 'F3V'
outfile = 'out.csv'
lower_value = 0.807375
upper_value = 0.807982

with open(infile, 'rb') as fin, open(outfile, 'w+b') as fout:
    arr = np.genfromtxt(fin, usecols=(0,1,2), delimiter='', dtype=float)
    mask = (arr[:, 0] >= lower_value) & (arr[:, 0] <= upper_value )
    arr = arr[mask]
    np.savetxt(fout, arr, fmt='%g')

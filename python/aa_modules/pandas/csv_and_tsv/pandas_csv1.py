#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

infile = 'data.csv'
colnames = ['col0', 'col1', 'col2']
df = pd.read_csv(infile, sep=" ", header = None,skiprows = 0,
                 comment='#',names=colnames)

print('{} {} {} {}'.format('\ndf =  :\n', df,'',''))
print('{} {} {} {}'.format('\ndf[\'col0\'] = :\n', df['col0'],'',''))

col0 = df['col0']
col1 = df['col1']

#plt.plot(col0,col1,'ro')
#plt.show()


# convert to list
col0 = df.col0.tolist()
col1 = df.col1.tolist()
col2 = df.col2.tolist()
print('{} {} {} {}'.format('\nlist col0 = ', col0,'',''))


#==============================================================================
# read in a file
#
infile = 'F3V'
colnames = ['col0', 'col1']
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('\ndf.head \n', df.head(),'',''))
print('{} {} {} {}'.format('\ndf[\'col0\'] = :\n', df.col0.head(),'',''))
#
#------------------------------------------------------------------------------

#plt.plot(df['wave'],df['flux'])
#plt.show()

col0 = df.col0
col1 = df.col1

plt.plot(col0,col1)
plt.show()


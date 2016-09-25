#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 17, 2016


# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read in dataframes
#==============================================================================
# read in a file
#
infile = 'a.csv'
colnames = ['angle', 'wave','trans','refl']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df1 = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
		 comment='#',names=colnames,usecols=(0,1,2,3))

print('{} {} {} {}'.format('df.head \n', df1.head(),'',''))
#------------------------------------------------------------------------------


#==============================================================================
# read in a file
#
infile = 'b.csv'
colnames = ['wave', 'flux']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df2 = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
		 comment='#',names=colnames,usecols=(0,1))
print('{} {} {} {}'.format('df.head \n', df2.head(),'','\n'))
#------------------------------------------------------------------------------


result = df1.append(df2, ignore_index=True)
print(result.head())
print("\n")



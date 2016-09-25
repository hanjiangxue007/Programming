#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pandas as pd
import numpy as np


# extract range
infile = 'F3V'
outfile = 'extract_range_pandas2.csv'
lower_value = 0.808185
upper_value = 0.809197


print('{} {} {}'.format('Reading file      :', infile, ''))
print('{} {} {}'.format('Writing to a file : ', outfile, ''))
df         = pd.read_csv(infile, usecols=(0,1,2), skiprows=57,sep='\s+')
df.columns = [ 'col0', 'col1' , 'col2']

df.ix[ (df['col0'] <=  lower_value) | (df['col0'] >=  upper_value) , ['col1','col2'] ] = 0



#print(df)
df.to_csv(outfile, header=None, index=None, mode='w', sep='\t')

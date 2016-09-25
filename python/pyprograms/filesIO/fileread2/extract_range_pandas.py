#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pandas as pd
import numpy as np


# extract range
infile = 'F3V'
outfile = 'extract_range_pandas.csv'
lower_value = 0.807375
upper_value = 0.807982


print('{} {} {}'.format('Reading file      :', infile, ''))
print('{} {} {}'.format('Writing to a file : ', outfile, ''))
df         = pd.read_csv(infile, usecols=(0,1,2), skiprows=57,sep='\s+')
df.columns = [ 'col0', 'col1' , 'col2']
df         = df[(df['col0'] >=  lower_value) & (df['col0'] <=  upper_value) ]
df.to_csv(outfile, header=None, index=None, mode='w', sep=' ')

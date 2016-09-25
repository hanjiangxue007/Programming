#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 17, 2016


# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#==============================================================================
# read in a file
#
infile = 'a.csv'
colnames = ['angle', 'wave','trans','refl']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
		 comment='#',names=colnames,usecols=(0,1,2,3))
df.wave = df.wave * 1000.0
print('{} {} {} {}'.format('df.head \n', df.head(),'','\n'))
#------------------------------------------------------------------------------
outfile = 'aa.csv'
df.to_csv(outfile,index=None,header=None,sep='\t')


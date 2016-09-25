#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==============================================================================
# read in a file
#
infile = 'psf_flux.txt'
colnames = ['col0', 'col1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('df.head \n', df.head(),'',''))
#col0 = df.col0.tolist()
#col0 = df.col0.tolist()
#------------------------------------------------------------------------------

sumcol1 = df.col1.sum()
print('{} {} {} {}'.format('\nsum col1 = ', sumcol1,'',''))


#==============================================================================
# read in a file
#
infile = 'psf_flux.txt'
colnames = ['col0', 'col1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
		 comment='#',names=colnames,usecols=(0,1))
print('{} {} {} {}'.format('df.head \n', df.head(),'',''))
#col0 = df.col0.tolist()
#col0 = df.col0.tolist()
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
 # Date      : May 23, 2016
 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in comments from the file
infile = 'filecopy_multiple.txt'
comments = []
with open(infile, 'r') as f:
    for line in f.readlines():
        if line.startswith('#'):
            comments.append(line)






#==============================================================================
# read in a file
#
infile = infile
colnames = ['angle', 'wave','trans','refl']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1,2,3))
print('{} {} {} {}'.format('length of df : ', len(df),'',''))


# write 20 files
df = df
nfiles = 20
nrows = int(len(df)/nfiles)
groups = df.groupby(   np.arange(len(df.index)) / nrows   )
for (frameno, frame) in groups:
    frame.to_csv("output_%s.csv" % frameno,index=None, header=None)

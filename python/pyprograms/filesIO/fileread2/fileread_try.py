#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read in a file
infile = 'F3V'
colnames= ['col0', 'col1']

df = pd.read_csv(infile,sep='\s+', names=colnames,usecols=(0,1))         # gives # as first column
df = pd.read_csv(infile,sep='\s+', names=None,usecols=(0,1),comment='#') # this also works
#df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 57,
                 #comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('df.head \n', df.head(),'',''))

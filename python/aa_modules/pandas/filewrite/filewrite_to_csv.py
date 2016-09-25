#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe to write
df = pd.DataFrame({ 'a': [ 1,2,3],
                    'b': [10,20,30],
		    'c': [100,200,300]
                   })

# write to a file
outfile = 'filewrite_to_csv.txt'
mycolumns = ["a","c"]
myheader = ['Apple', 'Cat']
myheader2 = list('AC')
df.to_csv(outfile, header=myheader,index=True,sep='\t',columns=mycolumns)

	#A	B
#0	1	100
#1	2	200
#2	3	300
#==============================================================================



# read in the file
infile = 'filewrite_to_csv.txt'
colnames = ['c0', 'c1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))

df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('\ndf.head \n', df.head(),'',''))

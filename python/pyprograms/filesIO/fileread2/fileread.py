#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://akuederle.com/stop-using-numpy-loadtxt

# As a quick comparison, loading ~500MB text file with loadtxt uses ~900MB of
# ram at peak usage, while loading the same file with genfromtxt uses ~2.5GB.

# Testfile: 250 mb (6215000 x 4 tab-separated datapoints)
#           using the ipython %timeit function for timing
# numpy.loadtxt: 36.6 s per loop
# pd.read_csv  : 2.36 s per loop

# pandas.read_csv is the fastest and faster than csv itself.

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cStringIO import StringIO


# using pandas.read_csv
#==============================================================================
# read in a file
#
infile = 'F3V'
colnames = ['col0', 'col1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 57,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('df.head \n', df.head(),'',''))
#col0 = df.col0.tolist()
#col0 = df.col0.tolist()
#plt.plot(df.col0,df.col1)
#plt.savefig('F3V.png')
#plt.show()
#------------------------------------------------------------------------------



# using numpy.loadtxt
#==============================================================================
#
# read in a file
infile = 'F3V'
print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
col0,col1 = np.loadtxt(infile, dtype=(float,float),skiprows=0, usecols=(0,1),
                       unpack=True,delimiter=None)
print('{} {} {} {}'.format('First row    : ', col0[0], col1[0],'\n ' ))
#plt.plot(wv,flx)
#plt.show()
#------------------------------------------------------------------------------



# using numpy.genfromtxt
#==============================================================================
# read in a file
#
infile = 'F3V'
print('{} {} {} {}'.format('\nreading file    : ', infile, '','' ))
col0,col1 = np.genfromtxt(infile,delimiter='',usecols=(0,1),dtype=None,unpack=True)
print('{} {} {} {}'.format('Number of lines : ', len(col0), '','' ))
print('{} {} {} {}'.format('First row       : ', col0[0], col1[0],'' ))
print('{} {} {} {}'.format('Last row        : ', col0[len(col0)-1], col1[len(col1)-1],'\n ' ))
#
#------------------------------------------------------------------------------




# using pythonic way
##=============================================================================
# read in a file
infile = 'F3V'
k=0
col0=[]
col1=[]
f=open(infile,'r')
for line in f:
   if not line.startswith("#"):
    row=line.split()
    col0.append(float(row[0]))
    col1.append(float(row[1]))
    k = k+1
f.close()
print (col0[0],col1[0])
print('{} {} {} {}'.format('no. of lines = ', k, ' ',' ' ))
print('{} {} {} {}'.format('type(col0[0] =  ', type(col0[0]), ' ',' ' ))
#------------------------------------------------------------------------------




# use StringIO to create data
#==============================================================================
# reading data using loadtxt
data = StringIO("1,0,2\n3,0,4")
col0, col1,col2 = np.loadtxt(data, delimiter=',', usecols=(0, 1,2), unpack=True)
print('{} {} {} {}'.format('First row    : ', col0[0], col1[0],col2[0] ))

#==============================================================================
# read in a file
data = StringIO("#this is comment\n1 0 2\n3 0 4")
col0, col1,col2 = np.genfromtxt(data, delimiter='', usecols=(0, 1,2), unpack=True,comments='#')
print('{} {} {} {}'.format('First row    : ', col0[0], col1[0],col2[0] ))





#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import numpy as np

##=============================================================================
# read in a file
infile = 'f3v1.txt'
infile = '3cols.dat'
x = np.genfromtxt(infile,delimiter=None,usecols=(0),dtype=str,unpack=True)
y,z = np.genfromtxt(infile,delimiter=None,usecols=(1,2),dtype=float,unpack=True)
print(x[0],y[0],z[0])
print(type(x[0]))
print(type(y[0]))





## read in a file
#infile = '3cols.dat'
#x = np.genfromtxt(infile,usecols=(0),delimiter=' ',dtype=str)
#y = np.genfromtxt(infile,usecols=(1),delimiter=' ',dtype=float)




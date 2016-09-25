#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np



# read data from the file
infile = 'psf_flux.txt'
x = np.genfromtxt(infile,delimiter=None,usecols=(0),dtype=str,unpack=True)
y = np.genfromtxt(infile,delimiter=None,usecols=(1),dtype=float,unpack=True)

# print data
print('{} {} {}'.format('x[0] = ',x[0], ''))


# example2
dt = (str,float)
x,y = np.genfromtxt(infile,delimiter=None,usecols=(0,1),dtype=dt,unpack=True)
print('{} {} {}'.format('x[0] = ',x[0], ''))

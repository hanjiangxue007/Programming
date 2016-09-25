#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 
#
# Inputs      : a fitsfile
# Outputs     : the total number
#
# Info:
# 1. This program will get the sum of all the pixels in a fitsfile.
#

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import time

infile = 'in0.fits'
data   = fits.getdata(infile)
shape  = data.shape

print('{} {} {}'.format('Reading data from: ',infile, '\n'))
print('{} {} {}'.format(r'data.shape[0] (rows) = ',data.shape[0], ''))
print('{} {} {}'.format(r'data.shape[1] (clms) = ',data.shape[1], '\n'))
print('{} {} {}'.format('data[0][0] = ',data[0][0], ''))
print('{} {} {}'.format('data[0] = ',data[0], ''))
print('{} {} {}'.format('sum data[0] = ',sum(data[0]), ''))
print('{} {} {}'.format('data[7] = ',data[7], ''))
print('{} {} {}'.format('sum data[7] = ',sum(data[7]), '\n'))

rows = data.shape[0]
total = 0.0
for i in range(rows):
    print('{} {} {}'.format(i, ': sum(data[i]) = ',sum(data[i])))
    total += sum(data[i])


print('{} {} {}'.format('\ntotal = ',total, ''))

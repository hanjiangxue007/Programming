#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pyfits as py
import numpy as np
import os


in1 = py.open('in1.fits') # 20*6 matrix bottom row 1 to 6


# Working with Image Data
data = in1[0].data
print(data[0]) # bottom row
print(len(data))
print(data[len(data)-1]) # top row


# make numpy array
data = np.array(data)
data_double = 2 * data
print("\n")
print(data_double)

# save changes to new fitsfile
outfile = 'out1.fits'
if os.path.exists(outfile):
    os.remove(outfile)


in1.writeto(outfile)
print('{} {} {} {}'.format('\nOutput file is:', outfile,'','\n'))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update :
#
# Inputs      : in1.fits
#               in2.fits
# Outputs     : difference.fits
#
# Info:
# 1. This program takes in two input fits file and creates 
#    difference of them.
# 
#
# Imports
from astropy.io import fits
import numpy as np
import subprocess
import time

# start time
start_time = time.time()

# get data shape from first input file
infile1 = 'in1.fits'
data1   = fits.getdata(infile1)
shape1   = data1.shape
print('{} {} {}'.format('Reading file: ', infile1, ''))
print('{} {} {}'.format(r'shape[0] = ',shape1[0], ''))
print('{} {} {}'.format(r'shape[1] = ',shape1[1], ''))
print('{} {} {}'.format('data1 300 300 = ',data1[300][300], ''))
print('{} {} {}'.format('ds9 image1 300 300 = ', '17.9202', '\n'))

# get data shape from first second file
infile2 = r'in2.fits'
data2   = fits.getdata(infile2)
shape2  = data2.shape
print('{} {} {}'.format('Reading file: ', infile2, ''))
print('{} {} {}'.format(r'shape[0] = ',shape2[0], ''))
print('{} {} {}'.format(r'shape[1] = ',shape2[1], ''))
print('{} {} {}'.format('data2 300 300 = ',data2[300][300], ''))
print('{} {} {}'.format('ds9 image2 300 300 = ', '6.96642', '\n'))


# output data
outfile = r'difference.fits'
dout = data1 - data2
hdu  = fits.PrimaryHDU()
hdu.data = dout
hdu.writeto(outfile, clobber=True)
print('{} {} {}'.format('dout 300 300 = ',dout[300][300], '\n'))

#output info
print('{} {} {}'.format('infile1     : ',infile1, ''))
print('{} {} {}'.format('infile2     : ',infile2, ''))
print('{} {} {}'.format('output file : ',outfile, ''))


# print the time taken
end_time = time.time()
seconds = end_time - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))

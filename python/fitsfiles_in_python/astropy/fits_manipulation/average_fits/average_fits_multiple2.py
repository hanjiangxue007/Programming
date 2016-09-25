#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# get data shape from first input file
infile1 = 'in1.fits.gz'
data1   = fits.getdata(infile1)
shape   = data1.shape
print('{} {} {}'.format(r'shape[0] = ',shape[0], ''))
print('{} {} {}'.format(r'shape[1] = ',shape[1], '\n'))
dout = np.zeros((shape[0],shape[1]))



# input filenames
infiles = []
nfiles = 4
for i in range(nfiles):
    tmp = 'in{:d}.fits.gz'.format(i)
    infiles.append(tmp)
    print(tmp)



for i in range(nfiles):
    infile   = infiles[i]
    data     = fits.getdata(infile)
    dout     = dout + data
    hdu      = fits.PrimaryHDU()
    hdu.data = dout
    hdu.writeto('sum.fits', clobber=True)

    if i == (nfiles-1):
        dout = dout/nfiles
        hdu  = fits.PrimaryHDU()
        hdu.data = dout
        hdu.writeto('average.fits', clobber=True)



# display image in ds9
command = '/Applications/ds9.app/Contents/MacOS/ds9 average.fits'
subprocess.call(command, shell = True)


# note:
# ds9 in0_tab &

# bottom rows of input files
# in0: 0 1 2 3
# in1: 0 2 4 6
# in2: 0 3 6 9
# in3: 0 4 8 12
################
# sum 0 10 20 30
# avg 0 2.5 5 7.5 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 15, 2016
# Last update : 
#
# Inputs      : fitsfiles
#               
# Outputs     : weighted_average.fits
#               
# Info:
# 1. This program creates weighted average of the input fitsfiles.
#    Algorithm: output = data_i * weight_i / sum(weight)
#

# Imports
from astropy.io import fits
import numpy as np

# weights
weight = np.linspace(1.0,4.0,num=4,endpoint=True)

# read data from first input file
dat = fits.getdata('psf/psf0.fits')

# make data all zero
dat = dat * 0.0

# average the data
nfiles = 4 # should be 21
for i in range(0,nfiles):
    infile = 'psf/psf{:d}.fits'.format(i)
    tmp    = fits.getdata(infile) * weight[i]
        
    # add data
    dat += tmp    
    
    if i ==(nfiles-1):
        dat = dat/sum(weight)

# create HDU objects to write fitsfiles
hdu      = fits.PrimaryHDU()
hdu.data = dat


# write to a fitsfile
outfile = 'weighted_average.fits'
hdu.writeto(outfile, clobber=True)

# output info
print('{} {} {}'.format('\noutput file: ',outfile, ''))

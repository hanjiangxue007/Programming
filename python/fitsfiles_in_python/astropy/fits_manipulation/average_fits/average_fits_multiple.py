#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from astropy.io import fits
import numpy as np

# read data from first input file
dat = fits.getdata('in0.fits.gz')
print('{} {} {}'.format('dat[0]= ',dat[0], ''))

nfiles = 4
for i in range(1,nfiles):
    infile = 'in{:d}.fits.gz'.format(i)
    tmp    = fits.getdata(infile)    
    dat    += tmp
    
    print('\n{} {} {}'.format('tmp[0]= ',tmp[0], ''))
    print('{} {} {}'.format('dat[0]= ',dat[0], ''))
    
    if i ==(nfiles-1):
        dat_avg = dat/nfiles

# create HDU objects to write fitsfiles
hdu1      = fits.PrimaryHDU()
hdu2      = fits.PrimaryHDU()
hdu1.data = dat
hdu2.data = dat_avg


# write to a fitsfile
outfile1 = 'sum2.fits'
outfile2 = 'average2.fits'
hdu1.writeto(outfile1, clobber=True)
hdu2.writeto(outfile2, clobber=True)

# output info
print('{} {} {}'.format('output file: ',outfile1, ''))
print('{} {} {}'.format('output file: ',outfile2, ''))

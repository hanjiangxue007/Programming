#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 15, 2016
# Last update : 
#
# Inputs      : fitsfiles
#               textfile
#               
# Outputs     : weighted_average.fits
#               
# Info:
# 1. This program creates weighted average of the 
#    input fitsfiles using weights from a textfile.

# Imports
from astropy.io import fits
import numpy as np



# get list of psf and weights
infile = 'psf_weight.txt'
psf    = np.genfromtxt(infile,delimiter=None,usecols=(0),
                       dtype=str,unpack=True)
weight = np.genfromtxt(infile,delimiter=None,usecols=(1),
                       dtype=float,unpack=True)

for i in range(len(psf)): 
    print('{} {} {} {}'.format(i,' : ',psf[i], weight[i]))
    
print('{} {} {}'.format('sum(weight) = ',sum(weight), ''))

# read data from first input file
dat = fits.getdata('psf/psf0.fits')
print('{} {} {}'.format('\ndat[0] = ',dat[0], ''))

# make data all zero
dat = dat * 0.0
print('{} {} {}'.format('dat[0] = ',dat[0], ''))

nfiles = 4
for i in range(0,nfiles):
    infile = 'psf/psf{:d}.fits'.format(i)
    tmp    = fits.getdata(infile)
    tmp2   = np.multiply(tmp,weight[i])

    
    # add data
    dat += tmp2
    
    # print
    print('{} {} {}'.format('\ninfile: ',infile, ''))
    print('tmp [0]: {} weight: {} tmp2[0]: {} dat[0]: {}'.format( 
           tmp[0],weight[i],tmp2[0],dat[0] ))
    
    
    if i ==(nfiles-1):
        dat_avg = dat/sum(weight)

# create HDU objects to write fitsfiles
hdu1      = fits.PrimaryHDU()
hdu2      = fits.PrimaryHDU()
hdu1.data = dat
hdu2.data = dat_avg


# write to a fitsfile
outfile1 = 'sum.fits'
outfile2 = 'weighted_average2.fits'
hdu1.writeto(outfile1, clobber=True)
hdu2.writeto(outfile2, clobber=True)

# output info
print('{} {} {}'.format('\noutput file: ',outfile1, ''))
print('{} {} {}'.format('output file: ',outfile2, ''))

# psf   bottom    weight  value
# psf0: 0 1 2 3    1      0 1 2 3
# psf1: 0 2 4 6    2      0 4 8 12
# psf2: 0 3 6 9    3      0 9 18 27
# psf3: 0 4 8 12   4      0 16 32 48
#########################################
#                         0 30 60 90  total wt = 10
#                         0 3  6  9



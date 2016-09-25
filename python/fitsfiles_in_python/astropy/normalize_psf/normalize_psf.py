#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 12, 2016
# Last update :
#
# Inputs      : 21 input psf from unnormalized psf directory
# Outputs     : 21 output psf inside normalized psf directory
#
# Info:
# 1. This program will get the sum of all the pixels in a fitsfile.
#
# Estimated time : 1 minute 22 seconds
#



# Imports
from astropy.io import fits
import numpy as np
import time


# beginning time
program_begin_time = time.time()
begin_ctime        = time.ctime()


# get sum of all pixels of psf10
infile = 'output_psfs/psf10.fits'
data   = fits.getdata(infile)
shape  = data.shape
rows = data.shape[0]
total_psf10 = 0.0
for i in range(rows):
    total_psf10 += sum(data[i])



for i in range(21):

    infile = 'output_psfs/psf{}.fits'.format(i)
    data   = fits.getdata(infile)
    shape  = data.shape

    rows = data.shape[0]
    total = 0.0
    for j in range(rows):
        total += sum(data[j])

    # update the data after getting total of all rows
    for k in range(rows):
        data[k] *= total_psf10/total

    # output data
    outfile = 'normalized_psf/psf' + str(i) + '.fits'
    hdu  = fits.PrimaryHDU()
    hdu.data = data
    hdu.writeto(outfile, clobber=True)

    #output info
    print('\n', infile)
    print('{} {} {}'.format('output file : ',outfile, ''))







# print the time taken
program_end_time = time.time()
end_ctime        = time.ctime()
seconds          = program_end_time - program_begin_time
m, s             = divmod(seconds, 60)
h, m             = divmod(m, 60)
d, h             = divmod(h, 24)
print('\nBegin time: ', begin_ctime)
print('End   time: ', end_ctime,'\n')
print("Time taken: {0:.0f} days, {1:.0f} hours, \
      {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))



#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 09, 2016
# Last update :
#
# Inputs      : given fitsfile
# Outputs     : sum of all the pixels in that fitsfile
#
# Info:
# 1. This program will get the sum of all the pixels in a fitsfile.
#
# Estimated time : 46 seconds
#



# Imports
from astropy.io import fits
import numpy as np
import time


# beginning time
program_begin_time = time.time()
begin_ctime        = time.ctime()



for i in range(21):

    infile = 'normalized_psf/psf{}.fits'.format(i)
    data   = fits.getdata(infile)
    shape  = data.shape

    rows = data.shape[0]
    total = 0.0
    for i in range(rows):
        total += sum(data[i])
    print('{} {} {}'.format(infile,' total = ',total))





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

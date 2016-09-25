#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 03, 2016
# Last update :

# Inputs      : none
# Outputs     : out1.fits,out2.fits

# Info:
# 1. This program creates fitsfiles.
 

# Imports
from astropy.io import fits
import numpy as np

# shape
shape0 = 601
shape1 = 601

NUM_FILES = 4
for i in range(NUM_FILES):

    # data to write    
    #data = np.ones((shape0,shape1)) * i
    data = np.array([[1,2,3,4],[5,6,7,8]]) * i

    # output file
    outfile = 'out{:d}.fits'.format(i)
    dout = data

    # create hdu and write data to it.
    hdu  = fits.PrimaryHDU()
    hdu.data = dout
    hdu.writeto(outfile, clobber=True)

    # print info
    print('{} {} {}'.format('dout 0 0 = ',dout[0][0], ''))
    print('{} {} {}'.format('output file : ',outfile, '\n'))




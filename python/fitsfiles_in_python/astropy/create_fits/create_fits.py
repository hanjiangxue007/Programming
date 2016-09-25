#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 03, 2016
# Last update :

# Inputs      : none
# Outputs     : out1.fits

# Info:
# 1. This program creates fitsfiles.
 

# Imports
from astropy.io import fits
import numpy as np


# shape


data = np.array([[1,2,3,4],[5,6,7,8]])

# output data
outfile = 'out1.fits'
dout = data
hdu  = fits.PrimaryHDU()
hdu.data = dout
hdu.writeto(outfile, clobber=True)
print('{} {} {}'.format('dout 0 0 = ',dout[0][0], '\n'))

#output info
print('{} {} {}'.format('output file : ',outfile, ''))




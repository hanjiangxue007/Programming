#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


# create an HDU object:
hdu = fits.PrimaryHDU()

# data
hdu.data = np.arange(32).reshape((8, 4))

# print header
print(hdu.header)


# set additional header keywords:
hdu.header['Author'] = 'Bhishan Poudel'


# write to a fitsfile
outfile = 'outputs/in1.fits.gz'
hdu.writeto(outfile, clobber=True)

# print output info
print('{} {} {}'.format('output file = ',outfile, ''))


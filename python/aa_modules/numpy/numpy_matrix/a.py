#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from __future__ import print_function
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
hdu.header['telescop'] = 'Python Observatory'


# write to a fitsfile
hdu.writeto('create_fits2.fits', clobber=True)


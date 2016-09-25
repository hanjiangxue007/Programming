#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from __future__ import print_function
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


# create HDU objects:
h0 = fits.PrimaryHDU()
h1 = fits.PrimaryHDU()
h2 = fits.PrimaryHDU()
h3 = fits.PrimaryHDU()

# data
d0 = h0.data = np.arange(32).reshape((8, 4))
d1 = h1.data = 2 * d0
d2 = h2.data = 3 * d0
d3 = h3.data = 4 * d0


# write to a fitsfile
h0.writeto('in0.fits', clobber=True)
h1.writeto('in1.fits', clobber=True)
h2.writeto('in2.fits', clobber=True)
h3.writeto('in3.fits', clobber=True)




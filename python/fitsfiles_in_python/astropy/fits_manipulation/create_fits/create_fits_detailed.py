#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://python4astronomers.github.io/astropy/fits.html

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Creating a FITS file from scratch
# If you want to create a FITS file from scratch, you need to start off
# by creating an HDU object:

hdu = fits.PrimaryHDU()

# and you can then populate the data and header attributes with
# whatever information you like:

hdu.data = np.random.random((128,128))


# Note that setting the data automatically populates the header with
# basic information:

print(hdu.header)


# and you should never have to set header keywords such as NAXIS, NAXIS1, and
# so on manually. We can then set additional header keywords:

hdu.header['telescope'] = 'Python Observatory'


# and we can then write out the FITS file to disk:

# hdu.writeto('random_array.fits')

# If the file already exists, you can overwrite it with:

hdu.writeto('random_array.fits', clobber=True)


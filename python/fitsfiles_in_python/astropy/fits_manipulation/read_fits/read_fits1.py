#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://python4astronomers.github.io/astropy/fits.html
# Download  : http://fermi.gsfc.nasa.gov/ssc/data/access/lat/BackgroundModels.html

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt




hdulist = fits.open('gll_iem_v02_P6_V11_DIFFUSE.fit')

# The returned object, hdulist, behaves like a Python list, and each element
# maps to a Header-Data Unit (HDU) in the FITS file. You can view more
# information about the FITS file with:

print(hdulist.info())


# As we can see, this file contains two HDUs. To access the primary HDU,
# which contains the main data, you can then do:

hdu = hdulist[0]

# The hdu object then has two important attributes: data, which behaves like
# a Numpy array, can be used to access the data, and header, which behaves like
# a dictionary, can be used to access the header information.
# First, we can take a look at the data:

print(hdu.data.shape)

# This tells us that it is a 3-d cube. We can now take a peak at the header

print("\n")
print(hdu.header[11])

# which shows that this is a Plate Carrée (-CAR) projection in
# Galactic Coordinates, and the third axis is photon energy.
# We can access individual header keywords using standard item notation:

print(hdu.header['TELESCOP'])


print(hdu.header['INSTRUME'])

# Provided that we started up ipython with the --matplotlib flag and did
# import matplotlib.pyplot as plt, we can plot one of the slices in photon energy:

plt.imshow(hdu.data[0,:,:], origin='lower')
#plt.show()


# Note that this is just a plot of an array, so the coordinates are just
# pixel coordinates at this stage. The data is stored with longitude increasing
# to the right (the opposite of the normal convention), but the Level 3 problem
# at the bottom of this page shows how to correctly flip the image.

# Modifying data or header information in a FITS file object is easy.
# We can update existing header keywords:

hdu.header['TELESCOP'] = "Fermi Gamma-ray Space Telescope"

# or add new ones:

hdu.header['MODIFIED'] = '26 Feb 2013'  # adds a new keyword

# and we can also change the data, for example extracting only the first
# slice in photon energy:

hdu.data = hdu.data[0,:,:]

# Note that this does not change the original FITS file, simply the FITS
# file object in memory. Note that since the data is now 2-dimensional,
# we can remove the WCS keywords for the third dimension:

hdu.header.remove('CRPIX3')
hdu.header.remove('CRVAL3')
hdu.header.remove('CDELT3')
hdu.header.remove('CUNIT3')
hdu.header.remove('CTYPE3')

# You can write the FITS file object to a file with:

hdu.writeto('lat_background_model_slice.fits')

# if you want to simply write out this HDU to a file, or:

hdulist.writeto('lat_background_model_slice_allhdus.fits')

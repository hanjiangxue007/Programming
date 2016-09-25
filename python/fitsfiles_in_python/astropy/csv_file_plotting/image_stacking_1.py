#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : http://www.astropy.org/astropy-tutorials/FITS-images.html

# Imports
from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import download_file
from astropy.io import fits

# Basic image math: image stacking
# You can perform math with the image data like any other numpy array.
# In this particular example, I will stack several images
# of M13 taken with a ~10'' telescope.

# I open a series of FITS files and store the data in a list,
# which I've named image_concat.

image_list = [ download_file('http://data.astropy.org/tutorials/FITS-images/M13_blue_000'+n+'.fits', cache=True ) \
              for n in ['1','2','3','4','5'] ]

# The long way
image_concat = []
for image in image_list:
    image_concat.append(fits.getdata(image))

# The short way
# image_concat = [ fits.getdata(image) for image in IMAGE_LIST ]
# Now I'll stack the images by summing my concatenated list.

# The long way
final_image = np.zeros(shape=image_concat[0].shape)

for image in image_concat:
    final_image += image

# The short way
#final_image = np.sum(image_concat, axis=0)
# I'm going to show the image, but I want to decide on the best stretch.
# To do so I'll plot a histogram of the data.

image_hist = plt.hist(final_image.flat, 1000)
#plt.show()

# I'll use the keywords vmin and vmax to set limits
# on the color scaling for imshow.

plt.imshow(final_image, cmap='gray', vmin=2.e3, vmax=3.e3)
plt.colorbar()
#plt.show()


# Writing image data to a FITS file
# This is easy to do with the writeto() method.

# You will receive an error if the file you are trying to write already exists.
# That's why I've set clobber=True.

outfile = 'stacked_M13_blue.fits'

hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, clobber=True)


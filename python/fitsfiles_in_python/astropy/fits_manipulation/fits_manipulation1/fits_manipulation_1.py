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


image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )


# Opening FITS files and loading the image data
# I will open the FITS file and find out what it contains.

hdu_list = fits.open(image_file)
print(hdu_list.info())


# image data
print("\n")
image_data = hdu_list[0].data
print(image_data)


print("\n")
print(type(image_data))

# At this point, we can just close the FITS file.
# We have stored everything we wanted to a variable.

hdu_list.close()
print(image_data.shape)

# SHORTCUT
# If you don't need to examine the FITS header, you can call
# fits.getdata to bypass the previous steps.
print("\n")
image_data = fits.getdata(image_file)
print(type(image_data))
print(image_data.shape)


# Viewing the image data and getting basic statistics
plt.imshow(image_data, cmap='gray')
plt.colorbar()
#plt.show()


# Let's get some basic statistics about our image
print("\n")
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))


# Plotting a histogram
# To make a histogram with matplotlib.pyplot.hist(),
# I need to cast the data from a 2-D to array to something one dimensional.

# In this case, I am using the iterable python object img_data.flat.
print("\n")
print(type(image_data.flat))
NBINS = 1000
histogram = plt.hist(image_data.flat, NBINS)

# Displaying the image with a logarithmic scale
# Want to use a logarithmic color scale?
# To do so we need to load the LogNorm object from matplotlib.

from matplotlib.colors import LogNorm
plt.imshow(image_data, cmap='gray', norm=LogNorm())

# I chose the tick marks based on the histogram above
cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])


#


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://python-astro.blogspot.com/2012/03/play-with-fits-files.html

# Imports
import pyfits
import numpy as np
import matplotlib.pyplot as plt

# create hdulist
hdulist = pyfits.open('n10017o.fits')

print(len(hdulist))

print("\n")
print(hdulist.info())

# The table said that there is only a primary HDU which
# contains 2154 X 2048 image with data stored in 2 bytes (16 bits) integers.

# As described above, the HDU (header/data unit) contains header and data.
# The header is a dictionary. To see what keywords were used in the
# header one can do:

print("\n")
print(hdulist[0].header.keys())

# and to get the value of a given keyword
print("\n")
print(hdulist[0].header['OBJECT'])

# The header can be printed as it apears in the file by
# this does not work in my laptop
# print (hdulist[0].header.ascardlist())


# The data in the file are accessible with

data = hdulist[0].data

# and can be seen with [don't forget to import matplotlib.pyplot as plt
# before running this]:

plt.imshow(data)

# A column from the data can be plotted with
plt.plot(data[:,1000])

# where I am plotting the column number 1000. In the same way a line
# from the data is plotted with:

plt.plot(data[1000,:])
plt.show()

# The data are numpy object so all manipulations are available.
# Some more on displaying images
# The main matplotlib function to display images is imshow.
# It has several parameters of which te most important are the one which
# controls the color scheme and the ones which control the dynamic range.

plt.imshow(data, cmap=cm.gray, vmin=1000, vmax=10000)

# cmap controls the pseudocolor map (same as color= in IDL).
# The predefined color maps can be seen on
# http://matplotlib.sourceforge.net/examples/pylab_examples/show_colormaps.html

# vmin and vmax controls the range of values which are mapped in [0,1] range
# where 0 is black (the darkest color) and 1 is white (the lightest color).

# origin = 'upper' | 'lower', place the pixel with coordinates 0,0 at the
# upper or lower corner of the plot

# extent = (xmin,xmax,ymin,ymax) - This parameter defines the numbers
# written on the axes. No changes on the image.

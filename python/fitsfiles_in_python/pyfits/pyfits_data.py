#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://pythonhosted.org/pyfits/

# Imports
import pyfits
import os

hdulist = pyfits.open('in1.fits')


##=============================================================================
# Working with Image Data
data = hdulist[0].data
print('{} {} {} {}'.format('\ndata.shape = ', data.shape,'','\n'))
print('{} {} {} {}'.format('\ndata.dtype.name = ', data.dtype.name,'','\n'))

# Since image data is a numpy object, we can slice it, view it, and perform
# mathematical operations on it. To see the pixel value at x=5, y=2:

# Note that, like C (and unlike FORTRAN), Python is 0-indexed and the indices have
# the slowest axis first and fastest changing axis last; i.e. for a 2-D image, the
# fast axis (X-axis) which corresponds to the FITS NAXIS1 keyword, is the second
# index. Similarly, the 1-indexed sub-section of x=11 to 20 (inclusive) and y=31 to
# 40 (inclusive) would be given in Python as:
# >>> scidata[30:40, 10:20]


print('{} {} {} {}'.format('\ndata[0] = ', data[0],'','\n'))
print('{} {} {} {}'.format('\ndata[len(data)-1] = ', data[len(data)-1],'','\n'))
print('{} {} {} {}'.format('\ndata[0][0] = ', data[0][0],'','\n'))

print('{} {} {} {}'.format('\ndata[0:2,0:2] = ', data[0:2, 0:2],'','\n'))


# To update the value of a pixel or a sub-section:
# >>> scidata[30:40, 10:20] = scidata[1, 4] = 999
# This example changes the values of both the pixel [1, 4] and the sub-section
# [30:40, 10:20] to the new value of 999. See the Numpy documentation for
# more details on Python-style array indexing and slicing.

print('{} {} {} {}'.format('\ndata[1,4] = ', data[1,4],'','\n'))


data[1,4] = 999
print('{} {} {} {}'.format('\ndata[1,4] = ', data[1,4],'','\n'))


# save changes to new fitsfile
outfile = 'newimage.fits'
if os.path.exists(outfile):
    os.remove(outfile)


hdulist.writeto(outfile)
print('{} {} {} {}'.format('\nOutput file is: ', outfile,'','\n'))

# If a file was opened with the update mode, the HDUList.flush() method
# can also be used to write all the changes made since open(), back to the
# original file. The close() method will do the same for a FITS file opened
# with update mode:

# >>> f = pyfits.open('original.fits', mode='update')
# ... # making changes in data and/or header
# >>> f.flush()  # changes are written back to original.fits
# >>> f.close()  # closing the file will also flush any changes and prevent
# ...            # further writing






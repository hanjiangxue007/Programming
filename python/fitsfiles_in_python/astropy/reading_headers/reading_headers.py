#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. This program reads the header names and their values from
#    fitsfiles.
# 
#
# Description :
#     hdulist is the file opened, e.g.
#          hdulist = fits.open('input.fits'
#          f       = fits.open('original.fits', mode='update')
#
# hdulist        : header data      writeto  append flush  close
# hdulist.header : keys   [0,1,etc]
# hdulist.data   : shape




# Imports
from astropy.io import fits


# get hdulist
hdulist = fits.open('input.fits')

# print info
print(hdulist.info())
print("\n")

# print all headers
print(repr(hdulist[0].header))

# print existing fits header
print('{} {} {}'.format('\nprinting headers:','', ''))
simple = hdulist[0].header['SIMPLE']
simple = hdulist[0].header[0]
print('{} {} {}'.format('simple = ',simple, ''))

# append a new header
prihdr = hdulist[0].header
prihdr.set('observer', 'Bhishan Poudel')
observer = hdulist[0].header['observer']
print('{} {} {}'.format('observer = ',observer, ''))

# add a comment
prihdr.comments['observer'] = 'He is a new observer'

# print header keys
print('{} {} {}'.format('\nprinting all headers','', ''))
print(list(prihdr))
print(list(prihdr.keys()))
print(list(prihdr[:2]))


# write changed file
hdulist.writeto('newimage.fits')

# close hdulist
hdulist.close()

## f = fits.open('original.fits', mode='update')
# making changes in data and/or header
#f.flush()  # changes are written back to original.fits
#f.close()  # closing the file will also flush any changes and prevent
            # further writing

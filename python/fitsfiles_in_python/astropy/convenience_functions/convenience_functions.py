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
# 1. Exaples of astropy.io convenience functions
#
#

# Imports
from astropy.io.fits import getheader
from astropy.io.fits import getval
from astropy.io.fits import getdata

##==============================================================
# getheader
hdr = getheader('in.fits')
print(repr(hdr))


# example 2
print('{} {} {}'.format('\nexample2','', ''))
bitpix = hdr['bitpix']         # get the value of the keyword
print('{} {} {}'.format('bitpix = ',bitpix, ''))

# add a header
hdr.set('FILTER', 'r')

# change header value
hdr['BITPIX'] = '-64'        # change the keyword value

##==============================================================
## getval
naxis = getval('in.fits', 'naxis', 0)  # get 1st extension's keyword value
print('{} {} {}'.format('naxis = ',naxis, ''))


##==============================================================
## getdata
dat = getdata('in.fits')  # get data
print('data 303 303 = ', dat[303][303])
data, hdr = getdata('in.fits', 0, header=True)
print('{} {} {}'.format('hdr[0] = ',hdr[0], ''))
print('{} {} {}'.format('hdr[0] = ',list(hdr.keys())[0], ''))

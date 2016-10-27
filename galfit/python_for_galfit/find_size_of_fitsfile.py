#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-19-2016 Wed
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function
from astropy.io import fits

infile ='f606w_gal0.fits'
infile ='f814w_gal0.fits'
data = fits.getdata(infile)
print('the size of image is = ', data.shape)






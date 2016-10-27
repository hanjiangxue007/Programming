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


data,header = fits.getdata("imgblock.fits", ext=2, header=True)
fits.writeto('block2.fits', data, header, clobber=True)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 27, 2016
 

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# input files
infile1 = 'in0.fits.gz'
infile2 = 'in1.fits.gz'

# read data
dat1 = fits.getdata(infile1)
dat2 = fits.getdata(infile2)
dat3 = 0.5 * (dat1 + dat2 )

# create HDU objects to write fitsfiles
hdulist = fits.PrimaryHDU()
hdulist.data = dat3


# write to a fitsfile
outfile = 'average.fits'
hdulist.writeto(outfile, clobber=True)



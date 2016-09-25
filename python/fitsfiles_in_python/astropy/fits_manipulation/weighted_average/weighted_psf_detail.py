#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 15, 2016
# Last update : 

# Inputs      : output_psfs/21_psfs_fitsfiles
#               psf_flux.txt  ( created by generate_psf_flux.py)
#               
# Outputs     : output_psfs/weighted_psf.fits
#               
# Info:
# 1. This program creates weighted average of the 21 psf files obtained from
#    phosim software.
#
#    Weights range is from 1.0 to 1.2 .
#    These are the average flux ratio of 100 f606 fitsfiles and 100 f814 fitsfiles.  
#    (refer: ~/phosim/simdatabase/average_flux_ratio.py)
#          
#
# Estimated time : 

# Imports
import astropy.io
from astropy.io import fits
from astropy.io.fits import getheader
from astropy.io.fits import getval
from astropy.io.fits import getdata
import numpy as np



# get list of psf and weights
infile = 'psf_flux.txt'
psf    = np.genfromtxt(infile,delimiter=None,usecols=(0),dtype=str,unpack=True)
weight = np.genfromtxt(infile,delimiter=None,usecols=(1),dtype=float,unpack=True)
print('{} {} {}'.format('First row : ',psf[0], weight[0]))


# 

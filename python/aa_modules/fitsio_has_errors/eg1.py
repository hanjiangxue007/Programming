#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-15-2016 Sat
# Last update :
#
#
# Imports
#!/usr/bin/env python
from __future__ import division
__version__ = 'v11.4 -- last edited on Oct-15-2016 Sat'
__help__ = ' print bhishan.__functions__ to see available functions.\n \
           print <functname>.__doc__ to see details'
__functions__ = ['IndexToDeclRa','DeclRaToIndex','fits_read','masking',
                 'DECRA_hpix','repeat_test','density_lrg','save_fits',
                 'pixel_0mask']

import numpy
import healpy
from numpy.lib.recfunctions import append_fields as append
import fitsio
import sys
import os

def fits_read(filename, header=False, columns=None):
    """ fits_read(filename, header=False, columns=None)
    Reads in specific columns of a fits file
    Args:
        filename: name of the input fits file
        header : True/False
        columns: list of desired columns
    Returns
        object , header (if True): object that includes information of columns
    """
    fx = fitsio.FITS(filename, upper=True)
    fxcolnames = fx[1].get_colnames()
    if columns is None:
       tscolumns = ['RA', 'DEC', 'COMP', 'TYCHOVETO']
       readcolumns = numpy.intersect1d(list(tscolumns), fxcolnames).tolist()
       assert readcolumns != [], "Columns are different than default"
    else:
       assert numpy.setdiff1d(columns, fxcolnames).tolist() == [], "Missing column"
       readcolumns = list(columns)
    #
    #
    data = fx[1].read(columns=readcolumns)
    if header:
       hdr = fx[1].read_header()
       fx.close()
       return data, hdr, fxcolnames
    else:
       fx.close()
       return data


fits_read('../test.fits')

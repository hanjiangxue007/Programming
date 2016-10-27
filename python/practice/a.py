#!/usr/bin/env python
from __future__ import division
__version__ = 'v11.4 -- last edited on Sat Oct 15 11:26:23 EDT 2016'
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

def map_read(filename, columns=None):
    """map_read(filename,columns=None)
    Takes the map filename and reads in columns
    By default, desired columns are ['HPIX','DEPTH','EBV']
    """
    mx = fitsio.FITS(filename, upper=True)
    mxcolnames = mx[1].get_colnames()
    if columns is None:
       tscolumns = ['HPIX', 'DEPTH', 'FRACGOOD','EBV']
       readcolumns =  numpy.intersect1d(list(tscolumns), mxcolnames).tolist()
       assert readcolumns != [], "Columns are different than default"
    else:
       assert numpy.setdiff1d(columns, mxcolnames).tolist() == [], "Missing column"
       readcolumns = list(columns)
    #
    #
    data = mx[1].read(columns=readcolumns)
    mx.close()
    return data

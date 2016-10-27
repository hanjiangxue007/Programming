#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-15-2016 Sat
# Last update :
#
#
# Imports
import fitsio
from fitsio import FITS,FITSHDR

# Often you just want to quickly read or write data without bothering to
# create a FITS object. In that case, you can use the read and write
# convienience functions.

# read all data from the first hdu with data
filename='test.fits'
data = fitsio.read(filename)

# read a subset of rows and columns from a table
data = fitsio.read(filename, rows=[35,1001], columns=['x','y'], ext=2)

# read the header, or both at once
h = fitsio.read_header(filename, extension)
data,h = fitsio.read(filename, ext=ext, header=True)

# open the file, write a new binary table extension, and then write the
# data from "recarray" into the table. By default a new extension is
# added to the file. use clobber=True to overwrite an existing file
# instead. To append rows to an existing table, see below.
fitsio.write(filename, recarray)

# write an image
fitsio.write(filename, image)

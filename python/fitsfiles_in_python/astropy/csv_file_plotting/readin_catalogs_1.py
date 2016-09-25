#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : http://www.astropy.org/astropy-tutorials/plot-catalog.html

# Imports
from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii

# Read in catalog information from a text file and plot some parameters
# Astropy provides functionality for reading in and manipulating tabular data
# through the astropy.table subpackage. An additional set of tools for reading
# and writing ASCII data are provided with the astropy.io.ascii subpackage,
# but fundamentally use the classes and methods implemented in astropy.table.

# We'll start by importing the ascii subpackage:




# For many cases, it is sufficient to use the ascii.read('filename') function
# as a black box for reading data from table-formatted text files.
# By default, this function will try to figure out how your
# data is formatted/delimited (by default, guess=True).

tbl = ascii.read("simple_table.csv")
print(tbl)

print("\n")
print(tbl["ra"])


# If we want to then convert the first RA (as a sexagesimal angle) to decimal
# degrees, for example, we can pluck out the first (0th) item in the column and
# use the coordinates subpackage to parse the string:

import astropy.coordinates as coord
import astropy.units as u

first_row = tbl[0] # get the first (0th) row
ra = coord.Angle(first_row["ra"], unit=u.hour) # create an Angle object
print("\n")
print(ra.degree) # convert to degrees
# 267.75



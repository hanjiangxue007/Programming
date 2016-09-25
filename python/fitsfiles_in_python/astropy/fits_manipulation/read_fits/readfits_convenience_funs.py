#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://python4astronomers.github.io/astropy/fits.html

# Imports
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


# In cases where you just want to access the data or header in a specific HDU,
# you can use the following convenience functions:

data = fits.getdata('gll_iem_v02_P6_V11_DIFFUSE.fit')
header = fits.getheader('gll_iem_v02_P6_V11_DIFFUSE.fit')

# To get the data or header for an HDU other than the first,
# you can specify the extension name or index.
# The second HDU is called energies, so we can do:

data = fits.getdata('gll_iem_v02_P6_V11_DIFFUSE.fit', extname='energies')

# or:

data = fits.getdata('gll_iem_v02_P6_V11_DIFFUSE.fit', ext=1)

# and similarly for getheader.

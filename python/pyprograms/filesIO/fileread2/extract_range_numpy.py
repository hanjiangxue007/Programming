#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pandas as pd
import numpy as np


# using numpy
infile = 'F3V'
outfile = 'out.csv'
lower_value = 0.807375
upper_value = 0.807982

print('{} {} {}'.format('Reading file    :', infile, ''))
print('{} {} {}'.format('Writing to file :', outfile, ''))

with open(infile, 'rb') as fin, open(outfile, 'w+b') as fout:
    arr = np.genfromtxt(fin, usecols=(0,1,2), delimiter='', dtype=float)
    mask = (arr[:, 0] >= lower_value) & (arr[:, 0] <= upper_value )
    arr = arr[mask]
    np.savetxt(fout, arr, fmt='%g')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/
# Execute   : python3 numpy_loadtxt_1.py


# Imports
import numpy as np


fname = 'eg6-a-student-data.txt'
dtype3 = np.dtype([('gender', '|S1'), ('bps', 'f8'), ('bpd', 'f8')])

def parse_bp(s):
    try:
        return float(s)
    except ValueError:
        return -99.

def reformat_lines(fi):
    for line in fi:
        line = line.replace('/',' ')
        yield line

with open(fname) as fi:
    gender, bps, bpd = np.loadtxt(reformat_lines(fi), dtype3, skiprows=9,
                usecols=(1,7,8),converters={7: parse_bp, 8: parse_bp},
                unpack=True)

print('{} {} {} {}'.format('bp systolic = ', bps,'\n\nbp diastolic',bpd))

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


# using pandas
#==============================================================================
# read in a file
#
infile = 'F3V'
print('{} {} {}'.format('Reading file :', infile, ''))
df         = pd.read_csv(infile, usecols=(0,1,2), skiprows=57,sep='\s+')
df.columns = [ 'wave', 'flux' , 'err']
df         = df[(df['wave'] >=  0.807375) & (df['wave'] <=  0.807982) ]
print (df)


# write to a file
outfile = r'extract_range_out.txt'
print('{} {} {}'.format('\nWriting to a file: ', outfile, ''))
df.to_csv(outfile, header=None, index=None, mode='w', sep=' ')


# using np.savetxt
outfile2 = r'extract_range_out2.txt'
print('{} {} {}'.format('\nWriting to a file: ', outfile2, ''))
np.savetxt(outfile2, df.values, delimiter='  ')


wave = list(df.wave)
print(wave[0])
print(type(wave))

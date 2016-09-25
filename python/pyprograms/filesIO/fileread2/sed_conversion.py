#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#==============================================================================
# read in a file
#
infile = 'F3V'
colnames = ['col0', 'col1']
print('{} {} {} {}'.format('\nreading file : ', infile, '','\n' ))
df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 57,
                 comment='#',names=colnames,usecols=(0,1))

print('{} {} {} {}'.format('Data before conversion: \n', df.head(),'',''))
#------------------------------------------------------------------------------
# wavelength 1um = 1000 nm
# flux 1 W m-2 um-1 = 0.1 ergs-1 cm-2 Angstrom-1

df.col0 = 1000.0 * df.col0
df.col1 = 0.1 * df.col1
print("\nData After conversion:")
print(df.head())



# write to a file
outfile = r'F3V_converted.csv'
print('{} {} {}'.format('\nWriting to a file: ', outfile, ''))
df.to_csv(outfile, header=None, index=None, mode='w', sep=' ')


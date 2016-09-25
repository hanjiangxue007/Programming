#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 04, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. This program writes data to a file.
#

# imports
from __future__ import print_function
import numpy as np


# data
x = [1.5,15, 150, 1500]
y = [4.5,45, 450, 4500]


# write to a file
outfile = 'filewrite_np.dat'
np.savetxt(outfile, list(map(list, zip(*[x,y]))),
           fmt='%s',delimiter=' ', newline='\n')
print('{} {} {}'.format('output file : ',outfile, ''))



# regular method
with open('filewrite2.dat', 'w') as fout:
    for i in range(len(x)):
        print('{: <8} {: <8}'.format(x[i], y[i]), file=fout)


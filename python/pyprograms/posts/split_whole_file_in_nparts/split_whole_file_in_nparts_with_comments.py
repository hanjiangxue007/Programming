#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


infile = r'input.txt'

with open(infile, 'r') as f:
    data = f.readlines()

##=============================================================================
# get number of comments line
comments_lines = 0
for line in data:
    if line.strip().startswith('#'):
        comments_lines += 1
    else:
        break

print('{} {} {}'.format('comment_lines = ',comments_lines, '\n\n'))




##=============================================================================
nfiles = 20
chunk_size = (len(data)-comments_lines)//nfiles

for i in range(nfiles):
    with open('temp/output_{:02d}.txt'.format(i), 'w') as f:

        # add equal chunk_size data to all files
        lower = comments_lines + i      * chunk_size
        upper = comments_lines + (i+1 ) * chunk_size
        
        f.write( ''.join (  data[:comments_lines] +  data  [lower :  upper ] ))

        # description
        print('{} {} {}'.format('lower = ',lower, ''))
        print('{} {} {}'.format('uppper = ',upper, ''))

        # add more lines to last file, if exist
        if (i == nfiles - 1) and (len(data) > upper):
            f.write(''.join(data[upper:]))

            # description
            print('{} {} {}'.format('\ni = ',i, ''))
            print('{} {} {}'.format('len data = ',len(data), ''))            
            print('{} {} {}'.format('comment_lines = ',comments_lines, ''))


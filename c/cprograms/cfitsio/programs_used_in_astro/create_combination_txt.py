#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 15, 2016
# Last update :
#

# Imports
import numpy as np

nfiles = 100
outfile = 'combination.txt'
print('{} {} {}'.format('Creating file: ',outfile, ''))
with open(outfile,'w') as f:
    for i in range(0,nfiles):
        blue = 'colors/f606w_gal{:d}.fits'.format(i)
        red  = 'colors/f814w_gal{:d}.fits'.format(i)
        out  = 'combination_out/combination_{:d}.fits'.format(i)
        line = blue + '  ' + red  + '  ' +  out +'\n'
        f.writelines(line)

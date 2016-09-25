#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# copy comments from one file to another
##=============================================================================
infile = 'copy_comments_from_file_in.txt'
outfile = 'copy_comments_from_file_out.txt'

# remove output file if exists
os.remove(outfile) if os.path.exists(outfile) else None


fi=open(infile,'r')
fo=open(outfile,'a')
comments = []
for line in fi:
   if line.startswith("#"):
    comments.append(str(line))
    fo.write(line)
fi.close()
print('{} {} {} {}'.format('\noutput file  = ', outfile,'',''))
print('{} {} {} {}'.format('no. of lines = ', len(comments), ' ',' ' ))
#------------------------------------------------------------------------------

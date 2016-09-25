#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# data frame
df = pd.DataFrame({'a':[1,2,3], 'b':[10,20,30]})

# write file with append
outfile  = 'write_comments.txt'
comment1 = '# My awesome comment\n'
comment2 = '# Here is another one\n'
print('{} {} {} {}'.format('\noutfile = ', outfile, ' ',' ' ))

# remove output file if exists
os.remove(outfile) if os.path.exists(outfile) else None

with open(outfile, 'a') as f:
    f.write(comment1)
    f.write(comment2)
    df.to_csv(f, header=None, index=None, mode='a', sep='\t')

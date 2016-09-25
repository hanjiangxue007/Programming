#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a data frame
df = pd.DataFrame({ 'a': [1,2,3],
                    'b': [10,20,30]
                  })


# write this df to existing file
outfile = 'filewrite_append.txt'


# append to a file
print('{} {} {} {}'.format('\noutfile = ', outfile, ' ',' ' ))
df.to_csv(outfile, header=False, mode = 'a',index=None,sep='\t')

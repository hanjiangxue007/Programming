#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : https://stackoverflow.com/questions/26082718/python-write-two-lists-into-two-column-text-file

# data
x=[1.5,2,3]
y=[4,5,6]



# using zip and csv
import csv
from itertools import izip
outfile = 'write_lists_to_file.csv'
with open(outfile, 'wb') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(izip(x, y))


# using numpy savetxt
import numpy as np
xarray = np.array([0,1,2,3,4,5])
yarray = np.array([0,10,20,30,40,50])
data = np.array([xarray, yarray])
data = data.T # transpose to make columns
outfile='outfile.dat'
np.savetxt(outfile, data, fmt=['%d','%d'])


# general method
bins = [ 1,2,3,4,5 ]
freq = [ 9,8,7,6,5 ]
f = open("test.csv", "w")
for i in xrange(len(bins)):
    f.write("{} {}\n".format(bins[i], freq[i]))
f.close()


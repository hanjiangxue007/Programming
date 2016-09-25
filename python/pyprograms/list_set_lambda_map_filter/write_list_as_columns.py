#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016

# data
x = [0.5,1e2,2e-14,3e-4,4.0,-5.05]
y = [0,10,20,30,40,50]
z = ['nepal','india','china','usa','bhutan','japan']

# write lists as columns
import csv
outfile = 'tmp.dat'
with open(outfile, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(x,y,z))


# write lists as columns
import numpy as np
np.savetxt('tmp.dat', np.array([x,y,z]).T, \
            fmt=['%s','%s','%s'],delimiter='\t')



# AttributeError: fmt has wrong shape.
#data = [x,y,z]
#np.savetxt('hello.txt', data, fmt=['%s','%s','%s'])


# create strings
mystr = []
for i in range(6):
    tmp = 'psf%d.fits'%(i,)
    mystr.append(tmp)

print(len(mystr))
print(mystr)

# write to a file
np.savetxt('tmp.dat', np.array([mystr,x,y]).T, \
	    fmt=['%s','%s', '%s'],delimiter='\t')



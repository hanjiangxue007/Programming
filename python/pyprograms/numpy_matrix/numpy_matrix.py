#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016


# Imports
from __future__ import print_function
import numpy as np
import pandas as pd

#==============================================================================
A = np.array([[1,2,3,4],[5,6,7,8]]) # Creates a 2D array with initialized values
print('{} {}{}'.format('\nA = \n', A,'\n' ))
print('{} {}{}'.format('A[0,1] = \n', A[0,1],'\n'))

# It is also possible to iterate over an array.
# In the case of a multi-dimensional array, this is done with respect to
# the first dimension.

for row in A:
    #print (row)
    for element in row:
	print (element)

#==============================================================================
a = np.ones((4, 5))
a[0] = 2
# we assign an array of dimension 0 to an array of dimension 1
print(a)
print("\n")
#==============================================================================
m = np.ones((3,5),dtype='int')
for row in m:
  print (str(row))

#==============================================================================
mymatrix = np.matrix([[1,2,3],
                      [10,20,30],
                      [100,200,300]])
def myfunction( x ):
    return sum(x)

print("\nexample 2:")
print (np.apply_along_axis( myfunction, axis=1, arr=mymatrix ))


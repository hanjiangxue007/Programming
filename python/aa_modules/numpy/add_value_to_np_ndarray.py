#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 21, 2016
# Ref       : https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html
# Ref       : https://stackoverflow.com/questions/22392497/how-to-add-a-new-row-to-an-empty-numpy-array 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# python way for pyton lists
arr = []
arr.append([1,2,3])
arr.append([4,5,6])
# arr is now [[1,2,3],[4,5,6]]
print("\n")
print(arr)

# numpy makes single array
arr = np.array([])
arr = np.append(arr, np.array([1,2,3]))
arr = np.append(arr, np.array([4,5,6]))
# arr is now [1,2,3,4,5,6]
print("\n")
print(arr)




##=============================================================================
array1 = np.array([1,2,3,4,5])
print('{} {} {}'.format('\narray1 = \n',array1, ''))
print('{} {} {}'.format('type array1 = ',type(array1), '\n'))

value = 400.0

# add this value to numpy ndarray
array2 = np.append(array1, value)
print('{} {} {}'.format('array2 = ',array2, ''))

##=============================================================================
# using concatenate
value = 400.0
addvalue = np.array([value])
array2 = np.concatenate((array1,addvalue))
print('{} {} {}'.format('array2 = ',array2, ''))

##=============================================================================
# example
a = np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
print("\n")
print(a)

##=============================================================================
# with axis
b = np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
print("\n")
print(b)
print("\n")
print(b[0])

##=============================================================================
# slow method
arr = np.empty((0,3), int)
arr = np.append(arr, np.array([[1,2,3]]), axis=0)
arr = np.append(arr, np.array([[4,5,6]]), axis=0) # 4 5 6 7 gives error
print('{} {} {}'.format('\n\nslow method: \n','', ''))
print(arr)

##=============================================================================
##=============================================================================
# fast method
l = []
for i in xrange(10):
    l.append([3*i+1,3*i+2,3*i+3])

l = np.asarray(l)
print("\n")
print(l)

# slow method
a = np.empty((0,3), int)
for i in xrange(10):
    a = np.append(a, 3*i+np.array([[1,2,3]]), 0)

print("\n")
print(a)


# using hstack and vstack
arr = np.array([])
arr = np.hstack((arr, np.array([1,2,3])))
# arr is now [1,2,3]

arr = np.vstack((arr, np.array([4,5,6])))  # 4 5 6 7 gives error
# arr is now [[1,2,3],[4,5,6]]






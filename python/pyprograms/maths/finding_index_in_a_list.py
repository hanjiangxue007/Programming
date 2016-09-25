#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 05, 2016
# Ref       : https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
 

# Imports
import numpy as np




# python way
lst = ["foo", "bar", "baz", "bar"]
item = 'bar'
indexes = [i for i, j in enumerate(lst) if j == item]
print('{} {} {}'.format('indexes     = ',indexes, ''))
print('{} {} {}'.format('first_index = ',indexes[0], ''))



##=============================================================================
## using numpy
##        0 1 2 3 4 5 6
array1 = [1,2,1,3,4,5,1]
item = 1
np_array = np.array(array1)    
item_index = np.where(np_array==item)
print('{} {} {}'.format('\n\nUsing numpy:','', ''))
print('{} {} {}'.format('index       = ',item_index, ''))
print('{} {} {}'.format('indexes     = ', item_index[0], ''))
print('{} {} {}'.format('first index = ',item_index[0][0], ''))
print('{} {} {}'.format('last index  = ',item_index[0][-1], ''))




##=============================================================================
# raises errors
lst = ["foo", "bar", "baz", "bar"]
idx = lst.index("bar")  # Raises Value error if not found
print('{} {} {}'.format('index = ',idx, ''))


# example 2
lst = [1.0, 2.0, 3.0]
idx = lst.index(3.0)
print('{} {} {}'.format('index = ',idx, ''))



##=============================================================================
arr = [5.1, 4.4, 5, 4.1]
arr = np.array(arr)
v = 4.2
idx = (np.abs(arr - v)).argmin()
print('{} {} {}'.format('\n\nnearest index = ',idx, '\n\n'))


# another example
myrange = np.arange(300,1200.2,step =0.1)
np_array = myrange
item     = 531.0    
item_index = (np.abs(np_array - item)).argmin()
print('{} {} {}'.format(r'myrange[2310]  = ',myrange[2310], ''))
print('{} {} {}'.format('index          = ',item_index, ''))
print('{} {} {}'.format('myrange[index] = ',myrange[item_index], ''))

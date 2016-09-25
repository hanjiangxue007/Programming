#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : http://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.ndarray.html

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd


x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print('{} {}'.format('x = \n', x ))
print('{} {}'.format('\ntype = ', type(x) ))

print('{} {}'.format('shape = ', x.shape ))
print('{} {}'.format('dtype = ', x.dtype ))


# The array can be indexed using Python container-like syntax:
print('{} {}'.format('\nx[1,2] = ', x[1,2] ))
# i.e., the element of x in the *second* row, *third*

# For example slicing can produce views of the array:
y = x[:,1]
print('{} {}'.format('\nx[:,1] = ', x[:,1] ))


y[0] = 9 # this also changes the corresponding element in x
print('{} {}'.format('\nset y[0] = 9', '' ))
print('{} {}'.format('\ny = ', y ))
print('{} {}'.format('x = ', x ))

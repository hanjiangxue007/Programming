#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 21, 2016
# Ref       : https://stackoverflow.com/questions/5205575/how-do-i-get-a-empty-array-of-any-size-i-want-in-python 

# Imports
from __future__ import print_function
import numpy as np




# create empty list with 10 empty elements
a = [0] * 10
print("\n")
print(a)
a[4] = 10
print("\n")
print(a)




#or

a = [None] * 10
print("\n")
print(a)
a[4] = 10
print("\n")
print(a)




##=============================================================================
big_array = [] #  empty regular list
for i in range(5):
    arr = i*np.ones((1,4)) # for instance
    big_array.append(arr)
big_np_array = np.array(big_array)  # transformed to a numpy array
print("\n")
print(big_np_array[0][0])

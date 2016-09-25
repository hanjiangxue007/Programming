#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : https://docs.scipy.org/doc/numpy/reference/generated/numpy.split.html#numpy.split 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# split
x = np.arange(9.0) # 8.0 gives error, use array_split instead
parts = np.split(x, 3)
print("\n")
print(parts)

# split with given ranges
x = np.arange(8.0)
parts = np.split(x, [3, 5, 6, 10])
print("\n")
print(parts)



# array_split
x = np.arange(8.0)
parts = np.array_split(x, 3)
print("\n")
print(parts)


# dsplit
# numpy.dsplit(ary, indices_or_sections)[source]

# Split array into multiple sub-arrays along the 3rd axis (depth).

# Please refer to the split documentation. dsplit is equivalent to split
# with axis=2, the array is always split along the third axis provided the
# array dimension is greater than or equal to 3.


x = np.arange(16.0).reshape(2, 2, 4)
print("\ndsplit: x\n")
print(x)

parts = np.dsplit(x, 2)
print("\ndsplit x,2 ")
print(parts)


parts = np.dsplit(x, np.array([3, 6]))
print("\n")
print(parts)

##=============================================================================
##  hsplit
# numpy.hsplit(ary, indices_or_sections)[source]

# Split an array into multiple sub-arrays horizontally (column-wise).

# Please refer to the split documentation. hsplit is equivalent to split
# with axis=1, the array is always split along the second axis regardless
# of the array dimension.


x = np.arange(16.0).reshape(4, 4)
print("\n")
print(x)


parts = np.hsplit(x, 2)
print("\n")
print(parts)


np.hsplit(x, np.array([3, 6]))
print("\n")
print(parts)

#With a higher dimensional array the split is still along the second axis.
x = np.arange(8.0).reshape(2, 2, 2)
print("\n")
print(x)


parts = np.hsplit(x, 2)
print("\n")
print(parts)

## end                                                              end    ##
##=============================================================================

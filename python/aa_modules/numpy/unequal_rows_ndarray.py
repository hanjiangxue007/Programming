#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 21, 2016
# Ref       : https://stackoverflow.com/questions/3386259/how-to-make-a-multidimension-numpy-array-with-a-varying-row-size 

# Imports
from __future__ import print_function
import numpy as np



lst1 = [0,1,2,3]
lst2 = [2,3,4]

nparr1 = [0,1,2,3]
nparr2 = [2,3,4]


arr = np.array([  lst1 , lst2   ], dtype=object)
nparr = np.array([  nparr1 , nparr2   ], dtype=object)
print("\n lists dtype = object")
print(arr)
print(arr[0])
print(arr[0][0])
print("\n ndarray dtype = object")
print(nparr)
print(nparr[0])
print(nparr[0][0])



##=============================================================================
cells = [np.array(a) for a in [[0,1,2,3], [2,3,4]]]
print("\n for loop in np array")
print(cells)
print(cells[0])
print(cells[0][0])


##=============================================================================
a = np.ones((3,))
b = np.ones((2,))
c = np.array([a, b])
print("\njagged arrays")
print(c)
print(c[0])


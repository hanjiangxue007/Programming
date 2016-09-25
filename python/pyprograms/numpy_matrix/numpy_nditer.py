#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       :

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd


a = np.arange(6).reshape(2,3)
print('{} {}{}'.format('a = \n', a,'\n' ))
for x in np.nditer(a):
    print (x,)

#==============================================================================
print('{} {}{}'.format('\na = \n', a,'\n' ))
a = np.arange(6).reshape(2,3)
for x in np.nditer(a.T):
        print (x,)
# 0 1 2 3 4 5

print('{} {}{}'.format('\na = \n', a,'\n' ))
for x in np.nditer(a.T.copy(order='C')):
    print (x,)

#==============================================================================
print('{} {}'.format('\n example', '' ))
a = np.arange(6).reshape(2,3)
print(a[0])


for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x

print(a[0])

#==============================================================================
a = np.arange(6).reshape(2,3)

print("\norder = F ")
for x in np.nditer(a, order='F'):
    print (x,)


print("\n order = C")
for x in np.nditer(a.T, order='C'):
    print (x)

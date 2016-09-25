#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016

# Program   : data except between a and b inclusive


# Imports
import numpy as np


# data
a = [1, 3, 5, 6, 9, 10, 14, 15, 56]
#    0  1  2  3  4  5    6  7    8    index

# find the indices for the given range in a list
a1 = np.where((np.array(a) >= 6) & (np.array(a) <=10))
a1 = np.where((np.array(a) >= 6) & (np.array(a) <=10))
print(a1)

# find the indices for the given range in a list
a1 = np.where(np.logical_and(np.array(a)>=6, np.array(a)<=10))
print(a1)

# find the indices for the given range in a list
a = [1, 3, 5, 6, 9, 10, 14, 15, 56]
start = np.searchsorted(a, 6, 'left')
end = np.searchsorted(a, 10, 'right')
rng = np.arange(start, end)
print(rng)

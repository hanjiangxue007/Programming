#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np


# given a list and tuple of index, find corrosponding elements

# data
a = [10, 11, 12, 13, 14, 15]

# method 1
a1 = [a[i] for i in (1,2,5)]
print(a1)

# method 2
numbers = range(10, 16)
indices = ( 1, 2, 5)
result = [numbers[i] for i in indices]
print(result)

# mehtod 3
s = [1, 2, 5]
a1 = list(np.array(a)[s])
print(a1)
#Better yet, just stay with Numpy arrays
a1 = np.array([10, 11, 12, 13, 14, 15])
print(a1[s])

# method 4
a1 =  [x[1] for x in enumerate(a) if x[0] in [1,2,5]]
print(a1)

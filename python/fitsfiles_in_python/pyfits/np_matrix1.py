#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.matrix.html

# Imports
import numpy as np

a = np.matrix('1 2; 3 4')
print (a)

vector1 = np.array([1, 2, 3])
vector2 = np.array([10, 20, 30])

b = np.matrix(vector1, vector2)

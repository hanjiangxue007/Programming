#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 15, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. multiply an array of string by converting to float and then by some number.
#
#

# Imports
import numpy as np

# array of strings and nan
arr = ['0.1', 'null', '0.2']

# assign a float value to nan string
arr[1] = np.nan

print(arr)
print('{} {} {}'.format('type(arr) = ',type(arr), ''))

## change data type
arr = [float(i) for i in arr]

## do the operation
tripled = np.array(arr) * 3

print(tripled)

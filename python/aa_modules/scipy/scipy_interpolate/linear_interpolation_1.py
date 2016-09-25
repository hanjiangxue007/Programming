#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : May 23, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. 
#

# Imports 
import scipy.interpolate

# data
x= [1, 2.5, 3.4, 5.8, 6]
y=[2, 4, 5.8, 4.3, 4]

# interpolater function
y_interp = scipy.interpolate.interp1d(x, y)

print (y_interp(5.0))



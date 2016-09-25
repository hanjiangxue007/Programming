#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 27, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. find the maxima of a function
#
#

# Imports
import scipy
import scipy.optimize


def f(x): return -2 * x**2 + 4 * x
max_x = scipy.optimize.fmin(lambda x: -f(x), 0)

print(max_x)

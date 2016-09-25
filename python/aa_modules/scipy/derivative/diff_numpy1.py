#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 28, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
#

# Imports
import numpy as np


# y = 1 * x^2 + 1
p = np.poly1d([1, 0, 1])
print (p)
   #2
#1 x + 1


# find derivative
q = p.deriv()
print (q)

#2 x


# find derivative at x = 5
q5 = q(5)
print('{} {} {}'.format('q(5) = ',q5, ''))

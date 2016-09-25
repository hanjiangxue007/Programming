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
from sympy import Symbol,lambdify
import numpy as np


x = Symbol('x')
y = x**2 + 1
yprime = y.diff(x)
print('{} {} {}'.format('yprime = ',yprime, ''))


f = lambdify(x, yprime, 'numpy')
ans = f(np.ones(5))
print('{} {} {}'.format('ans = ',ans, ''))

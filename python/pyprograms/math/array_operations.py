#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Feb 18, 2016


# Imports
import numpy as np


# parametric equations and array mathematics
t = np.arange(1, 6, 1)
x = np.square(t)
y = np.power(t,3)
z = np.array((t)**2+1)
print(t,x,y,z)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 24, 2016


# Imports
import numpy as np

t = np.arange(2, 10, 2) ; print(t)
t1 = np.arange(1, 4, 0.5) ; print(t1)  # last digit is not included
t3 = np.arange(0, 2*np.pi, 0.1)

x = np.square(t) ; print(x)

y = np.array( (t)**3 - 3*t ); print(y)

z = np.array( (-1/t) ); print(z)
z1 = np.array( (-1.0/t) ); print(z1)
z2 = np.array( (-1.0/(t**2)) ); print(z2)



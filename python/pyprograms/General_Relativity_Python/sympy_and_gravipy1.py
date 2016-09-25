#!/usr/bin python
# -*- coding: utf-8 -*-

# Bhishan Poudel
# Feb 14, 2016

# Ref: http://www.linuxjournal.com/content/general-relativity-python

# Imports
from sympy import *
from gravipy import *

x,y,z = symbols('x y z')

t, r, theta, phi = symbols('t, r, \\theta, \phi')

x = Coordinates('\chi', [t, r, theta, phi])

print(x(-1))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 03, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#

# Imports
from __future__ import print_function

import numpy as np
from scipy.integrate import simps
from numpy import trapz

##=============================================================================
# read in a file
infile = 'F3V_first'
print('{} {} {} {}'.format('\nreading file : ', infile, ' ',' ' ))
x,y = np.genfromtxt(infile,delimiter=None,usecols=(0,1),dtype=float,unpack=True)
##=============================================================================


# Compute the area using the composite Simpson's rule.
area = simps(y)
print("area =", area)

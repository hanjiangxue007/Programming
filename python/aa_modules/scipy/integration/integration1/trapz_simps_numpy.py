#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 03, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. This program calculates the integraton.
#


# Imports
import numpy as np
from scipy.integrate import trapz, simps

x, dx = np.linspace(-100, 250, 50, retstep=True)
mean, sigma = 90, 20
f = np.exp(-((x-mean)/sigma)**2/2) / sigma / np.sqrt(2 * np.pi)
print('{:18.16f}'.format(np.sum(f)*dx))
print('{:18.16f}'.format(trapz(f, x)))
print('{:18.16f}'.format(simps(f, x)))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 11, 2016

# Imports
import scipy
from scipy.constants import h,N_A
from scipy.constants import physical_constants as pc

print ("The Planck constant h:", h)
print ("The Avogadro constant N_A:", N_A)
print ("The muon mass in u:", pc['muon mass in u'])


a = scipy.constants.physical_constants["alpha particle mass"]
print('{} {} {}'.format('a = ',a, ''))
print('{} {} {}'.format('a[0] = ',a[0], ''))

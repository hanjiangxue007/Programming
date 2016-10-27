#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-08-2016 Sat
# Last update :
#
#
# Imports
from natu.units import degC, K
from natu.units import km,m,s,kg


a = 0*degC + 100*K
print('\n')
print(a)

print(km/m)

##======================================================================
a =  1*kg*m**2/s**2
print('\n')
print(a)




##======================================================================
## fractions
##======================================================================
from fractions import Fraction
a =  m**Fraction(1, 2)
print('\n')
print(a)

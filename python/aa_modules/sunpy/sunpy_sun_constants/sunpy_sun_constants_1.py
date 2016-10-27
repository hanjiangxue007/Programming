#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-16-2016 Sun
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function
import sunpy
from sunpy.sun import constants as con
from sunpy.sun.constants import luminosity

# one astronomical unit (the average distance between the Sun and Earth)
print (con.au)
print("\n")
print('{} {} {}'.format('con.radius*2 = ',con.radius*2, ''))

print("\n")
print('{} {} {}'.format('con.radius.to("km").value = ',con.radius.to('km').value, ''))


print('{} {} {}'.format('luminosity = ',luminosity, ''))

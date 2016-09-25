#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 04, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. This program groups a list into n parts
#

# Imports
from itertools import zip_longest

# function 
def grouper(n, iterable, padvalue=None):
  "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
  return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

# usage
l = [1,2,3,4,5,6,7,8,9]

l1 = grouper(3, 'abcdefg', 'x')

print('{} {} {}'.format('type l1 = ',type(l1), ''))


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np


# extract range between 4 and 8 inclusive
a = [ 1,2,3,4,5,6,7,8,9]
b = [x for x in a if (x>=4 | x<=8) ]
print(b)


# example
numbers = [1,2,3,4,5]
doubled_odds = [n*2 for n in numbers if n%2 == 1]


# example
l = [1, 10, 15, 25, 30]
l1 =  [x+1 if x >= 10
      else x+5
      for x in l]


print(l1)


# extract range between 4 and 8 inclusive
a = [ 1.5,2,3,4,5,6,7,8,9]
b = [x for x in a if (x>=4.0) if (x<=8)]
print(b)


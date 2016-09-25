#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. Example of *args and **kwargs
# args = arguments
# kwargs = keyword arguments
#

# Imports
import operator
from functools import reduce


mynum = 1000
mystr = 'Hello World!'
print ("{mystr} New-style formatting is {mynum}x more fun!"  \
         .format(**locals()))


# example 2
def multiply(*args):
    return print(reduce(operator.mul, args))
    
# usage
multiply(1,2,3)
numbers = [1,2,3]
multiply(*numbers)

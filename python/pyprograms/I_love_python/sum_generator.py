#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 16, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
#

def sum_greater(x, y):
    return sum(i for i in x if i>y)



x = [1,3,5]    
a = sum_greater(x,4)
print(a)
##======================================================================

x = [1,2,4]
b = sum(i for i in x if i>6)
print(b)

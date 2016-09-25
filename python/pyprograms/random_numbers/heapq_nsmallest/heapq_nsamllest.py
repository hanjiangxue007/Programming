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
# 1. This program heaps the smallest numbers from a list
#

# Imports
import random,heapq


# create a list
a = [random.randint(0,100) for __ in range(100)]

b = heapq.nsmallest(5,a)
c = heapq.nlargest(5,a)
print(b)
print(c)

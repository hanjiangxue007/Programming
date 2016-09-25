#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 26, 2016


# method 1 : use a list comprehension
a1 = [0,1,2]
a2 = [x * 3 for x in a1]
print (a2)

# method 2 : using numpy
import numpy
a3 = numpy.array(a1, dtype=int)*3
print (a3)

# method 3 : using map and lambda
a4 = list(map(lambda x:3*x, a1))
print(a4)

#e.g.2
mylist = [1, 2, 3, 4, 5]
scalar = 10
result = map(lambda x: x * scalar, mylist)
print(result)

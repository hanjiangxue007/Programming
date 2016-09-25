#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np

# data
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

sum_vector = vector1 + vector2
print (sum_vector)


# using zip
list1=[1, 2, 3]
list2=[4, 5, 6]
mysum = [sum(x) for x in zip(list1, list2)]
print(mysum)


# Using map with operator.add
from operator import add
mysum = map(add, list1, list2)
print(mysum)


listadd = np.array(list1) + np.array(list2)
print('{} {} {} {}'.format('\nlist add = ', listadd,'','\n'))

list1double = 2 * np.array(list1)
print('{} {} {} {}'.format('\nlist1double =', list1double,'','\n'))

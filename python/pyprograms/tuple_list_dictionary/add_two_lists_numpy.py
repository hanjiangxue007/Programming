#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list


# Imports
import numpy as np
import itertools


first = [1,2,3,4,5]
second = [6,7,8,9,10]

# best
three = [x + y for x, y in zip(first, second)]
print(three)

# using itertools
myListOfLists  = [first,second]
three = [sum(sublist) for sublist in itertools.izip(*myListOfLists)]
print(three)

# without using zip
three = [first[i]+second[i] for i in xrange(len(first))]
print(three)


# using sum and zip
three = [sum(i) for i in zip(first,second)] # [7,9,11,13,15]
print(three)


# using numpy
three = np.add(first, second)
print(three)

# using map sum zip
third = map(sum, zip(first, second))
print(three)



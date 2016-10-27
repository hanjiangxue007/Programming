#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 05, 2016
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function
import collections
from string import ascii_lowercase
from collections import OrderedDict

a = OrderedDict(zip(ascii_lowercase, range(5)))
print(a)


a = OrderedDict(zip(ascii_lowercase, range(6)))
print(a)

a = OrderedDict(zip(ascii_lowercase, range(7)))
print(a)

# also note:
print('\nexample 2')
a = collections.OrderedDict(a=1,b=2,c=3)
print(a)

# OrderedDict([('a', 1), ('c', 3), ('b', 2)])  # NOT IN ORDERED LIST!
# This seems like a bug, but as explained in the documentation,
# it happens because the keyword arguments are first processed as a
# normal dict before they are passed on to the OrderedDict.

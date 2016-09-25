#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

# Imports
from __future__ import division
from __future__ import print_function

# python 2
print("python 2 using map\n")
myList = ['abc', 'xyz'];
print("\n".join(map(str, myList))) # using map

# python 3 needs future import
print("\nUsing python 3")
print(*myList, sep='\n')

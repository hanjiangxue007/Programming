#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 06, 2016
# Last update :
#
# Ref: http://blog.rtwilson.com/my-top-5-new-python-modules-of-2015/
#
# Imports
items = list(range(5))
for item in items:
    print(item)
    #process your code here


# Just wrap the iterable in the tqdm function:

from tqdm import tqdm
for item in tqdm(items):
    print(item)

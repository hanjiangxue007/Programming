#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python

# Imports
from __future__ import division
from __future__ import print_function
import pprint


# For Python2
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

mylist = list(chunks(range(10, 80), 10))
pprint.pprint(mylist)

# For Python3
print("\n")
def chunks3(l, n):
    """Yield successive n-sized chunks from l."""
    yield [l[i:i+n] for i in range(0, len(l), n)]

pprint.pprint(list(chunks3(range(10, 75), 10)))


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list-with-python

# Imports
from __future__ import division
from __future__ import print_function

#\n included:
fname = 'input.dat'
fname = 'input2.txt'
with open(fname) as f:
    content = f.readlines()
print(content)

# \n excluded:
print("\n")
with open(fname) as f:
    content = f.read().splitlines()
print(content)

# sort alphabetically
print("\n")
print(sorted(content))

# sort
print("\n")
content.sort()
print(content)

# print line by line
print("\n")
print ('\n'.join([ str(myelement) for myelement in content ]))

# print space separated
print("\n")
print (' '.join([ str(myelement) for myelement in content ]))


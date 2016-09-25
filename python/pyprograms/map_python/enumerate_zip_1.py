#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016
# Ref     : http://www.saltycrane.com/blog/2008/04/how-to-use-pythons-enumerate-and-zip-to/

# Imports
from __future__ import division
from __future__ import print_function

# enumerate
alist = ['a1', 'a2', 'a3']
for i, a in enumerate(alist):
    print (i, a)


# zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
print("\n")
for a, b in zip(alist, blist):
    print (a, b)


# enumerate and zip
print("\n")
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print (i, a, b)





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

# zip return a list of tuples, where each tuple contains the i-th element
# from each of the argument sequences.  The returned list is truncated
# in length to the length of the shortest argument sequence.

# Imports
from __future__ import division
from __future__ import print_function


#In python 2.7 this might have worked fine.

a=b=c=range(5)
tuple_1 = zip(a,b,c)
print(tuple_1)
print("\n")
print(len(tuple_1[0]))


#But in python 3.4
print("\n")
a=b=c=range(5)
tuple_1 = list(zip(a,b,c))
print(tuple_1)


# example of zip
print("\n")
myzip = zip( range(5), range(1,20,2) )
print(myzip)
print(range(1,20,2))


# example of zip
print("\n")
c={'Bhihsan':'31','Pari':'28','Raj':'50','Sita':'45'}
d={'USA':'Washington DC','Rwanda':'Kigali','Belgium':'Brussels','Nepal':'Kathmandu'}
print(zip(c,d))

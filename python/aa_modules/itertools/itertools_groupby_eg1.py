#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-23-2016 Sun
# Last update :
#
#
# Imports
from itertools import groupby

# Eliminate consecutive duplicates
L=[1,1,1,1,1,1,2,3,4,4,5,1,2]
a = [x[0] for x in groupby(L)]
print(a)


##======================================================================
from operator import itemgetter
a = map(itemgetter(0), groupby(L))
print(a)

b = [x for x,y in groupby(L) if len(list(y))<2]
print('{} {} {}'.format('len > 2 = ',b, ''))

b = [x for x,y in groupby(L) if sum(1 for i in y)<2]
print('{} {} {}'.format('len > 2 = ',b, ''))


##======================================================================
from itertools import groupby
L = [1,1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1]
longest_consecutive = max(sum(1 for i in g) for k,g in groupby(L))
print('{} {} {}'.format('longest_consecutive = ',longest_consecutive, ''))


##======================================================================
print("\n")
data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in groupby(enumerate(data), lambda (i, x): i-x):
    #print (map(itemgetter(1), g))
    pass


# group number and consecutive frequency
my_list=[1,1,1,1,1,1,2,3,4,4,5,1,2]
b = [ [k,list(g).count(k) ] for k,g in groupby(my_list) ]
print(b)

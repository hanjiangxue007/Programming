#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : https://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
# Ref       : https://docs.scipy.org/doc/numpy/reference/generated/numpy.split.html


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





#==============================================================================
# slice into n parts
lst = range(20, 87)
nchuncks = 4
parts = np.array_split(lst,nchuncks)
print("\n")
print(parts[0])
print(parts[1])
print(parts[2])
print(parts[3])
print(parts[len(parts)-1])
print('{} {} {}'.format('lenght of list = ',len(lst), ''))
print('{} {} {}'.format('length of parts = ', len(parts), ''))
print('{} {} {}'.format('no. of elemtns in first part = ', len(parts[0]), ''))
print('{} {} {}'.format('no. of elemtns in last part = ', len(parts[len(parts)-1]), ''))
print('{} {} {}'.format('length of parts = ', len(parts), '\n'))

#==============================================================================
# slice into n elements
lst = range(20, 87)
nelements = 4
parts = np.array_split(lst,(len(lst)//nelements))
print("\n")
print(parts[0])
print(parts[1])
print(parts[2])
print(parts[3])
print(parts[len(parts)-1])
print('{} {} {}'.format('lenght of list = ',len(lst), ''))
print('{} {} {}'.format('length of parts = ', len(parts), ''))
print('{} {} {}'.format('no. of elemtns in first part = ', len(parts[0]), ''))
print('{} {} {}'.format('no. of elemtns in last part = ', len(parts[len(parts)-1]), ''))
print('{} {} {}'.format('length of parts = ', len(parts), '\n'))

#==============================================================================
# example
lst = range(531,696)
nchuncks = 20
parts = np.array_split(lst,nchuncks)
for i in range(len(parts)-1):
    print('{} {}{}{}'.format('len parts', i, ' = ', len(parts[i]) ))





#==============================================================================
# slice with each parts have n elemments
chunks = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

# test the function
lst = range(20, 87)
print('{} {}'.format('len lst = ', len(lst) ))
nelements = 4
parts = chunks(lst,nelements)

print(parts[0])
print(parts[1])
print(parts[2])
print(parts[3])
print(parts[len(parts)-1])
print('{} {} {}'.format('\n\nno. of elements in first part = ', len(parts[0]), ''))
print('{} {} {}'.format('no. of elements in last part = ', len(parts[len(parts)-1]), ''))
print('{} {} {}'.format('length of parts = ', len(parts), ''))




#==============================================================================
# slice with each parts have n elemments
chunks = lambda lst, sz: [lst[i:i+sz] for i in range(0, (len(lst)), sz)]

# test the function
lst = range(531, 696)
print('{} {}'.format('\n\nlen lst = ', len(lst) ))
nchuncks = 20
nelements = len(lst)/nchuncks
parts = chunks(lst, nelements)

for i in range(len(parts)):
    print('{} {}{}{}'.format('len parts', i, ' = ', len(parts[i]) ))


print('{} {}'.format('\nparts[19]', parts[19] ))


#==============================================================================
def partition(lst, n):
    division = len(lst) / float(n)
    return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n) ]

a = partition([1,2,3,4,5],5)
print('{} {}'.format('\na = ', a ))
a = partition([1,2,3,4,5],2)
print('{} {}'.format('\na = ', a ))

a = partition([1,2,3,4,5],3)
print('{} {}'.format('\na = ', a ))

parts = partition(lst, 20)
print("\n")
for i in range(len(parts)):
    print('{} {}{}{}'.format('len parts', i, ' = ', len(parts[i]) ))




#==============================================================================
## generator
#def chunks(l, n):
    #n = max(1, n)
    #return [l[i:i + n] for i in range(0, len(l), n)]
    ##return (l[i:i+n] for i in xrange(0, len(l), n))  # for generator


###=============================================================================
## using numpy
#x = np.arange(9.0) # 8.0 gives error
#parts = np.split(x, 3)
#print("\n\n")
#print(parts)


#x = np.arange(8.0)
#parts = np.split(x, [3, 5, 6, 10])
#print("\n")
#print(parts)
#==============================================================================



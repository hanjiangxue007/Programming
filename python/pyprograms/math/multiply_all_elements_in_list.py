#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 26, 2016

# method 1
product = 1  # Don't use 0 here, otherwise, you'll get zero because anything times zero will be zero.
list = [1, 2, 3]
for x in list:
    product *= x

print (product)

# method 2: using function
def product_list(p):
          total =1 #critical step works for all list
          for i in p:
             total=total*i # this will ensure that each elements are multiplied by itself
          return total

print product_list([2,3,4,2]) #should print 48

# method 3 : using numpy
import numpy as np
mylist = [1, 2, 3, 4, 5, 6]
result = np.prod(np.array(mylist))
print(result)

# method 4 : using reduce
result1 = reduce(lambda x, y: x*y, [1,2,3,4,5,6])
print(result1)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np

# data
l = [[1,2,3],[4,5,6],[7,8,9]]
x = [1.5,15, 150, 1500]
y = [4.5,45, 450, 4500]
z = ['nepal', 'india', 'usa','china']

# transpose a list
lt = list(map(list, zip(*l)))
print(lt[0])

# transpose a list
lt = np.asarray(l).T.tolist()
print(lt[1])

# transpose a list
lt = map(list,map(None,*l))
print(lt[0])

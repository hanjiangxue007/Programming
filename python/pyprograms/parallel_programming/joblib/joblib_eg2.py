#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 01, 2016
# Last update :
#
# Inputs      : none
#
# Outputs     :
#
# Info : https://blog.dominodatalab.com/simple-parallelization/
#
#
#



# Imports
from joblib import Parallel, delayed



# function
def func(a, b):
    return a + b

# run in parallel
args=[[1,2], [3,4] ]
results = Parallel(n_jobs=-1)(delayed(func)(i,j) for i,j in args)

# print
print(results)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. Calculate fibnonacci series.
#
#

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# usage
n= 10
for i in range(n):
    print(fib(i), end=" ")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. minimum no. of weights to weigh 1 to 40 pounds.
#
# Ref: http://www.python-course.eu/python3_memoization.php

# Our exercise is an old riddle, going back to 1612. 
# The French Jesuit Claude-Gaspar Bachet phrased it. 
# We have to weigh quantities (e.g. sugar or flour) from 1 to 40 pounds. 
# What is the least number of weights that can be used on a balance 
# scale to way any of these quantities. 

def factors_set():
    factors_set = ( (i,j,k,l) for i in [-1,0,1] 
                          for j in [-1,0,1]
                          for k in [-1,0,1]
                          for l in [-1,0,1])
    for factor in factors_set:
        yield factor

def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper

@memoize
def linear_combination(n):
    """ returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27      """
    weighs = (1,3,9,27)
      
    for factors in factors_set():
       sum = 0
       for i in range(len(factors)):
          sum += factors[i] * weighs[i]
       if sum == n:
          return factors
          
def weigh(pounds):
    weights = (1,3,9,27)
    scalars = linear_combination(pounds)
    left = ""
    right = ""
    for i in range(len(scalars)):
        if scalars[i] == -1:
            left += str(weights[i]) + " "
        elif scalars[i] == 1:
            right += str(weights[i]) + " "
    return (left,right)
 
# usage
for i in range(40):    
    print(weigh(i))

#!/usr/bin/env python
#author: bhishan poudel
#cmd   : clear; python fn4.py

def fn1(n): #eg. argument n = 4
    return n + 1      # output: 5
    
def fn2(n): # argument n = 10
    return fn1(n) * 2 #output: (10+1) * 2
    
print fn1(4)
print fn2(10)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 06, 2016
# Last update :
#
#
# Imports
import random

def runner(f, callable):
    def inner(*args, **kwds):
        for i in range(10):
            pos = list(callable())
            pos.extend(args)
            f(*pos, **kwds)
    return inner

def f(a, b, c, d = 3):
    print (a, b, c, d)

# call the runner and function
runner(f, lambda: (random.randint(1,10),)   )(3, 5, d = 7)

print('{} {} {}'.format('\nrunning function alone','', ''))
f(1,4,5,44)

print('{} {} {}'.format('\nexample of random.randint','', ''))
print(random.randint(1,10))

print('{} {} {}'.format('\nexample of lambda function','', ''))
a=lambda: (random.randint(1,10),) (3)
print(a)

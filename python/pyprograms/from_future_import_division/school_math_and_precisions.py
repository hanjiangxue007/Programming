#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

a = 1.33
b = 1.27
print(a + b) #2.6000000000000001
print(a * b) #1.6891
print(a + b) #2.6
print(a * b) #1.6891

print('\nusing decimal module')
from decimal import *
a = Decimal('1.33')
b = Decimal('1.27')
print(a + b)

Decimal('2.60')
print(a * b)
Decimal('1.6891')
print(a + b) #2.60
print(a * b) #1.6891
getcontext().prec = 4
print(a * b) #1.689
getcontext().prec = 3
print(a * b) #1.69

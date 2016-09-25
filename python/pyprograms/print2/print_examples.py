#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#

# Imports
import sys

a =  3.564
print("a = ", a)
print("a = \n", a)

# using sep
print('{} {} {}'.format('\nuse of sep','\n', ''))
print("a","b")
print("a","b",sep="")
print(192,168,178,42,sep=".")
print("a","b",sep=":-)")

# use of end
print('{} {} {}'.format('\nuse of end','', ''))
for i in range(4):
    print(i, end=" ")

# write to a file
with open('out.txt','w') as fout:
    print("42 is the answer, but what is the question?", file=fout)
    
# write to standard error log
print('{} {} {}'.format('\n\nuse of sys.stderr','', ''))
print("Error: 42", file=sys.stderr)
    
print("This line is after the errror.")

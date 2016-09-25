#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : https://stackoverflow.com/questions/16017419/python-read-log-files-and-get-lines-containing-specific-words 

# Imports
from __future__ import print_function
import numpy as np
import os



##=============================================================================
# method 1
infile = r"in.txt"

important = []
keep_phrases = ["test", "important","keep me"]

with open(infile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break

#print(important[0])






##=============================================================================
# method 2
with open("in.txt", 'r') as f:
    for line in f:
        if "test" in line:
            #print (line)
            pass




##=============================================================================
# get line numbers
breakpoints = np.arange(301.0,302.0,step = 0.1)
breakpoints = np.append(breakpoints, [302.0])



infile = r"input.txt"
outfile = r'output.txt'

important = []
keep_phrases = list(breakpoints)

idx = 0
lin_num = []
tmpidx = 0
os.remove(outfile) if os.path.exists(outfile) else None
with open(infile,'r') as fi, open(outfile, 'a') as fo:
    data = fi.readlines()
    for line in data:
        idx += 1
        for phrase in keep_phrases:
            #if str(phrase) in line:
            if line.startswith(str(phrase)):
                #print("\n")
                #print(line,end='')
                fo.write(line)
                tmpidx = idx
                #print(tmpidx)
                lin_num.append(tmpidx)
                pass
                
print('{} {} {}'.format('\nlin_num = \n',lin_num, ''))




##=============================================================================
# get indices in a file for a given list
lst1 = np.arange(301.0,302.0,step = 0.1)
lst1 = np.append(lst1, [302.0])
infile = r"input.txt"
idx = 0
lin_num = []
tmpidx = 0
with open(infile,'r') as fi:
    data = fi.readlines()
    for line in data:
        idx += 1
        for value in list(lst1):
            if line.startswith(str(value)):
                tmpidx = idx
                lin_num.append(tmpidx)                
print('{} {} {}'.format('\nlin_num = \n',lin_num, ''))



 


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 18, 2016


# Imports
from __future__ import print_function
import fileinput


# read in comments from the file
infile = 'data_with_comments.txt'
comments = []
with open(infile, 'r') as fi:
    for line in fi.readlines():
        if line.startswith('#'):
            comments.append(line)

# reverse the list
comments = comments[::-1]
print(comments[0])
#==============================================================================


# preprepend a list to a file
filename = 'test.txt'

for i in range(len(comments)):
    with file(filename, 'r') as original: data = original.read()
    with file(filename, 'w') as modified: modified.write(comments[i] + data)

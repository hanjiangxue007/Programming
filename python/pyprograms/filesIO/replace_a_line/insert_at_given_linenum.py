#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 26, 2016


# Imports
from __future__ import print_function
import fileinput


infile = 'input'
fobj =  fileinput.input(files = infile, inplace = True, backup = '.bak')
for line in fobj:
    if fileinput.lineno() == 1:
	line_insert = 'this is line1'
        print(line_insert)
    else:
        print(line, end='')
fobj.close()


# note: python 2.7 does not have 'WITH' context manager for FILEINPUT module

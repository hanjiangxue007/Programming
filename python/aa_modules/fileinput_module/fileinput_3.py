#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 23, 2016
# Ref       : https://stackoverflow.com/questions/30835090/attributeerror-fileinput-instance-has-no-attribute-exit

# Imports
from __future__ import print_function
import fileinput



##=============================================================================
def proc(line):
     parts = line.split(" ") # split line into parts
     if  "10" in line:    # if at least 2 parts/columns
         print (parts[1] +  ' ' + parts[2] + ' ' + parts[3] ) # print column 2 



f = fileinput.input(files=('spam.txt', 'eggs.txt'))

for line in f:
    proc(line)

f.close()



# The problem is that as of python 2.7.10, the fileinput module does not support
# being used as a context manager, i.e. the with statement, so you have to handle
# closing the sequence yourself. The following does not work:

# with fileinput.input(files=('spam.txt ', 'eggs.txt ')) as f:

# Note that in recent versions of python 3, you can use this module as a context manager.

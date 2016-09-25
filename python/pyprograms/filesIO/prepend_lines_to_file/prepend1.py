#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 18, 2016
# Ref       : http://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file

# Imports
from __future__ import print_function
import fileinput

# In mode 'a' or 'a+' , any writing is done at the end of the file, even if
# at the current moment when the write() function is triggered the file's
# pointer is not at the end of the file: the pointer is moved to the end of
# file before any writing. You can do what you want in two manners.

# 1st way, can be used if there are no issues to load the file into memory:

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

# loading file into memory
filename = 'a1.txt'
line = '# added line'
line_prepender(filename, line)

#==============================================================================
# not loading whole file into the memory
#
def line_pre_adder(filename, line_to_prepend):
    f = fileinput.input(filename, inplace=1)
    for xline in f:
        if f.isfirstline():
            print (line_to_prepend.rstrip('\r\n') + '\n' + xline,)
        else:
            print (xline,)
# usage:
filename = 'a1.txt'
line_to_prepend = 'line to prepend'
#line_pre_adder(filename,line_to_prepend)

# There's no way to do this with any built-in functions, because it would be
# terribly inefficient. You'd need to shift the existing contents of the
# file down each time you add a line at the front.

# There's a Unix/Linux utility tail which can read from the end of a file.
# Perhaps you can find that useful in your application.


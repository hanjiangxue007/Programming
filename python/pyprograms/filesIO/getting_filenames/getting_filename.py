#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 07, 2016
 

# Imports
import os
import sys


# method 1
script_name =  os.path.basename(sys.argv[0])
print('{} {} {}'.format('script name = ',script_name, ''))


# method 2
script_name = sys.argv[0]
print('{} {} {}'.format('script name = ',script_name, ''))


# method 3
script_name = os.path.basename(__file__)
print('{} {} {}'.format('script name = ',script_name, ''))




# If you call python linkfile.py, where linkfile.py is a symlink to realfile.py,
# sys.argv[0] will be 'linkfile.py', which may or may not be what you want;
# it is certainly what I expect. __file__ is the same: it will be linkfile.py.
# If you want to find 'realfile.py' from 'linkfile.py',
# try os.path.realpath('linkfile.py')

filename = script_name[0:-3]
print('{} {} {}'.format('filename = ',filename, ''))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 23, 2016
# Ref       : http://www.leancrew.com/all-this/2011/08/python-and-fileinput/ 

# Imports
from __future__ import print_function
import fileinput,sys


##=============================================================================
for line in fileinput.input():
    if line.startswith('bhi'):
        print (line)

# python using_command_args.py /usr/share/dict/words



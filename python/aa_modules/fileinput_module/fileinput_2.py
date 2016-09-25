#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 23, 2016
# Ref       : http://www.leancrew.com/all-this/2011/08/python-and-fileinput/ 

# Imports
from __future__ import print_function
import fileinput,sys


##=============================================================================
for line in open('/usr/share/dict/words'):
    if line.startswith('bhi'):
        print (line)



# from command line:   for line in open(sys.argv[1]):
# python a.py /usr/share/dict/words
##=============================================================================

for line in fileinput.input('/usr/share/dict/words', inplace=False):
    if line.startswith('bhi'):
        print (line[0])

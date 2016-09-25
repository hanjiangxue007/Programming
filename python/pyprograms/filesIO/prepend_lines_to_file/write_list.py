#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 18, 2016
# Ref       : http://stackoverflow.com/questions/2677617/python-f-write-at-beginning-of-file

# Imports
from __future__ import print_function



l=[]
l.append("string 1")
l.append("string 2")
l.append("string 3")

with open('write_list.txt','w'):
    for line in l:
        f.write(line + "\n")

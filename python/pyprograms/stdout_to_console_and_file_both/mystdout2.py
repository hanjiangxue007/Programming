#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016
 

# Imports
import sys


class Tee(object):
    def __init__(self, f1, f2):
        self.f1, self.f2 = f1, f2
    def write(self, msg):
        self.f1.write(msg)
        self.f2.write(msg)

outfile = open('outfile', 'w')

sys.stdout = outfile
sys.stderr = Tee(sys.stderr, outfile)

print("hello")

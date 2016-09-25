#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 07, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports
import dis

class Bar(object):
    y = 2

    def __init__(self, x):
        self.x = x

class Foo(object):
    def __init__(self, x):
        self.y = 2
        self.x = x

dis.dis(Bar)
dis.dis(Foo)

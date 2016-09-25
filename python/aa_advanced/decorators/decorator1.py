#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 08, 2016
# Last update :
#
# Depends     : none
#
# Outputs     :
#
# Info:
# 1.
#
#

# Imports
import os

def Exists(oldFunc):
    def inside(filename):
        if (os.path.exists(filename)):
            oldFunc(filename)
        else:
            print("File Does Not Exist")
    return inside

@Exists
def outputLine(inFile):
    with open(inFile) as f:
        print (f.readlines())


func = Exists(outputLine)
func("example.py")
func("test.py")

outputLine("example.py")

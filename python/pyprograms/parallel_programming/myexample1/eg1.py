#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 29, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
#

# Imports
from subprocess import Popen
from os import mkdir

argfile = open('commandline.txt')
for number, line in enumerate(argfile):    
    newpath = 'scatter.%03i' % number 
    mkdir(newpath)
    cmd = '../abc.py ' + line.strip()
    print ('Running %r in %r' % (cmd, newpath))
    Popen(cmd, shell=True, cwd=newpath)

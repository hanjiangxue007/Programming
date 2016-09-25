#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 15, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. creating list from file.
#

# list 
psf,outfile     = [],[] 

# store lines to list
with open('psf.txt',"r") as f: psf     = f.readlines()
with open('out.txt',"r") as f: outfile = f.readlines()

## print the list
for i in range(len(psf))    : print(psf[i], end= '')
for i in range(len(outfile)): print(outfile[i], end = '')

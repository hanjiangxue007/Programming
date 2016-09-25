#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 08, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

# Imports
import pyximport; pyximport.install()
import rbf

# to compile: python setup.py build_ext --inplace
# gives: rbf.c and rbf.so

# test from ipython:
# from rbf import rbf_network
# %timeit rbf_network(X, beta, theta)


# comparison: 
# vanilla python : 7.67 seconds = 7670 ms
# cython         : 247 ms

# other cython commands:
# cython rbf.pyx -a && open rbf.html 
      
# Note: this creates html 
#        yellow line are NOT cythonized
#        yellow lines inside loop are BAD!


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 23, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. Example of subprocess
#

# Imports
from __future__ import print_function
import subprocess


commands = " " +\
"echo 'hi' ; " +\
"touch junk1 ; " +\
"echo 'junk1 created' ; " +\
"echo 'hello' ; " +\
"echo 'output of ls' ;" + \
"ls"


print("Running commands :\n", commands, "\n")
subprocess.call(commands,shell=True)


##=============================================================================
# example 2

commands = " " +\
" echo 'hi' ; " +\
" echo 'hi2' ; " +\
" ls"


print("\nRunning commands :\n", commands, "\n")
subprocess.call(commands,shell=True)


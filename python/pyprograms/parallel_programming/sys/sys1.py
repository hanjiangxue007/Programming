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
import sys

def myscript(iteration_number):
    xfile_name = "x%d.txt" % iteration_number
    yfile_name = "y%d.txt" % iteration_number
    with open(xfile_name, "w") as xf:
        with open(yfile_name, "w") as yf:
            print(iteration_number, file=xf)
            print(iteration_number, file=yf)

def main(unused_command_line_args):
    for i in range(10):
        myscript(i)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 10, 2016
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
from multiprocessing import Pool

def f(x):
    return x*x

class Calculate(object):
    def run(self):
        p = Pool()
        return p.map(f, [1,2,3])

if __name__ == '__main__':
    cl = Calculate()
    print (cl.run())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: http://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments

# Imports
import os
from multiprocessing import Pool

def task(args):
    print ("PID =", os.getpid(), ", arg1 =", args[0], ", arg2 =", args[1])

pool = Pool()

pool.map(task, [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ])

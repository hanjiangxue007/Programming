#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: http://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments

# Imports
import multiprocessing as mp
from joblib import Parallel,delayed
from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support

def multi_run_wrapper(args):
   return add(*args)


def add(x,y):
    return x+y


if __name__ == "__main__":
    from multiprocessing import Pool
    pool = Pool(4)
    results = pool.map(multi_run_wrapper,[(1,2),(2,3),(3,4)])
    print (results)

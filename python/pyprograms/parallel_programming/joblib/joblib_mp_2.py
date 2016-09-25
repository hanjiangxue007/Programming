#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: http://scicomp.stackexchange.com/questions/19586/parallelizing-a-for-loop-in-python

# Imports
import multiprocessing as mp
from joblib import Parallel,delayed



def myfun(arg):
     result = arg**2
     return result


# args
arg_instances = [1,2,6]


results = Parallel(n_jobs=-1, backend="threading")(
             map(delayed(myfun), arg_instances))

print(results)



#joblib.Parallel(n_jobs=1,     -1 will use all cpu cores
    # backend=None,           'multiprocessing' is default, 'threading' (if code permits open GIL)
    # verbose=0,              if >0 prints info of iterations
    # timeout=None,           float, TimeOUtError will be raised after this time
    # pre_dispatch='2 * n_jobs',
    # batch_size='auto',
    # temp_folder=None,
    # max_nbytes='1M',
    # mmap_mode='r'

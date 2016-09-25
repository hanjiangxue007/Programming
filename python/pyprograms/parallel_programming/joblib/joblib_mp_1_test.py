#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 11, 2016
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
import time
from joblib import Parallel, delayed
import multiprocessing

def processInput(i):
    return i*i

if __name__ == '__main__':
    start = time.time()

    # time = 0.0010852813720703125
    results = list()
    print("Hello World!")
    inputs = range(1000)
    for i in inputs:
        results.append(processInput(i))
    print(results)

    mid = time.time()
    print("Time taken by usual approach: ", mid-start)

    # time = 0.13438153266906738
    results = list()
    print("Hello World!")
    intputs = range(1000)
    num_cores = multiprocessing.cpu_count()

    print(num_cores)

    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)

    print(results)
    end = time.time()


    print("Time taken by usual approach    : ", mid-start)
    print("Time taken by parallel approach : ", end-mid)

    print("Factor = ", (end-mid) / (mid-start) )












#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 01, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Ref: http://www.davekuhlman.org/python_multiprocessing_01.html
# 
#
#

# Imports
import argparse
import operator
from multiprocessing import Process, Queue
import numpy as np
import py_math_01
from functools import reduce

def run_jobs(args):
    """Create several processes, start each one, and collect the results.
    """
    queue01 = Queue()
    queue02 = Queue()
    queue03 = Queue()
    queue04 = Queue()
    m = 4
    n = 3
    process01 = Process(target=f_multiproc, args=(queue01, 'process01', m, n))
    process02 = Process(target=f_multiproc, args=(queue02, 'process02', m, n))
    process03 = Process(target=f_multiproc, args=(queue03, 'process03', m, n))
    process04 = Process(target=f_multiproc, args=(queue04, 'process04', m, n))
    process01.start()
    process02.start()
    process03.start()
    process04.start()
    input('Check for existence of multiple processes, then press Enter')
    process01.join()
    process02.join()
    process03.join()
    process04.join()
    input('Check to see if they disappeared, then press Enter')
    print(queue01.get())
    print(queue02.get())
    print(queue03.get())
    print(queue04.get())

def f_multiproc(queue, processname, m, n):
    seed = reduce(operator.add, [ord(x) for x in processname], 0)
    np.random.seed(seed)
    result = py_math_01.test_01(m, n)
    result1 = result.tolist()
    result2 = 'Process name: {}\n{}\n-----'.format(processname, result1)
    queue.put(result2)

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,)
    args = parser.parse_args()
    run_jobs(args)

if __name__ == '__main__':
    #import ipdb; ipdb.set_trace()
    main()

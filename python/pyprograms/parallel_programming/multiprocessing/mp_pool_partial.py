#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: http://python.omics.wiki/multiprocessing_map/multiprocessing_partial_function_multiple_arguments

# Imports
import multiprocessing
from functools import partial

def parallel_runs():
    pool = multiprocessing.Pool(processes=4)
    input_list = [1, 2, 3, 4]
    prod_x=partial(prod_xy, y=10) #prod_x has only one argument x (y is fixed to 10)    
    result_list = pool.map(prod_x, input_list) 
    print(result_list)
   
def prod_xy(x,y):
    return x * y

if __name__ == '__main__':
    parallel_runs()

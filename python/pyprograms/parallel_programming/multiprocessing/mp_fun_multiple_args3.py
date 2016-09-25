#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: http://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments

# Imports
from multiprocessing.dummy import Pool as ThreadPool

def write(i, x):
    print(i, "---", x)

a = ["1","2","3"]
b = ["4","5","6"] 


# starmap works python >= 3.3
pool = ThreadPool(2)
pool.starmap(write, zip(a,b)) 
pool.close() 
pool.join()

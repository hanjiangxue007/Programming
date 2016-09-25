#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#
# Ref: https://pythonhosted.org/joblib/parallel.html

# Imports
import multiprocessing,joblib
from time import sleep
from joblib import Parallel, delayed
from math import sqrt



# eg1

res = Parallel(n_jobs=1)(delayed(sqrt)(i**2) for i in range(10))
print(res)




# eg2
#r = Parallel(n_jobs=2, verbose=2)(delayed(sleep)(.1) for _ in range(10)) 


# eg3
from operator import neg

with joblib.parallel_backend('threading'):
     print(Parallel()(delayed(neg)(i + 1) for i in range(5)))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 19, 2016
# Last update : 
#

# Imports
import multiprocessing as mp
from joblib import Parallel,delayed
from multiprocessing import Pool

def computation(args):
    length, startPosition, npoints = args
    print(args)

length = 100
nproc=4
p = Pool(processes=nproc)
p.map(computation, [(startPosition,startPosition+length//nproc, length//nproc) for startPosition in  range(0, length, length//nproc)])

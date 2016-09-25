#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 29, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. multiprocess example
#
#

# Imports
from multiprocessing import Pool
import multiprocessing as mp


def func_sq(x):
    return x*x


pool = Pool(processes=4)

lst = [ i*3 for i in range(10) if i%2 == 0]
x = pool.map(func_sq, lst)

print(x)

##==============================================================================
# example 2
#

sim_seed_lst = [829220411,830004608,830072905,829174853,830071621,830082017,830083311]
nloop = len(sim_seed_lst)



def imcat_analysis(seed):
    sim_seed = seed
    print(seed)


pool = mp.Pool(processes=4)
x = pool.map(imcat_analysis,sim_seed_lst )

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
# Info: https://www.youtube.com/watch?v=q_zTtyq4EbE
# 1. 
#
#

# Imports
import time

# beginning time
program_begin_time = time.time()
begin_ctime        = time.ctime()

# cpu bound task
def do_something(n):
    val = 0
    for i in range(n):
        for x in range(i):
            val += x
    return val 
    
    
do_something(10000)
do_something(10000)
do_something(10000)
do_something(10000)
do_something(10000)
    
	    

# print the time taken
program_end_time = time.time()
end_ctime        = time.ctime()
seconds          = program_end_time - program_begin_time
m, s             = divmod(seconds, 60)
h, m             = divmod(m, 60)
d, h             = divmod(h, 24)
print('\nBegin time: ', begin_ctime)
print('End   time: ', end_ctime,'\n')
print("Time taken: {0:.0f} days, {1:.0f} hours, \
      {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

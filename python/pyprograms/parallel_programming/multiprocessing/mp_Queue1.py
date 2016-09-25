#!/usr/bin/python3
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
# Ref: https://rcc.fsu.edu/docs/high-performance-computing-python
#
#
#


# Example: To compare the performance of a parallel python script with that of a 
# serial one, we need to run some task that is CPU intensive. 
# In the following Python script, the function primeQ(n) tells you if the input 
# integer n is a prime or not; the function sumPrimes(n) computes the sum of all 
# prime numbers less than a given integer n. 
# This take some CPU time if n is a large number.
 
# 1. We create a Queue object to store a list of large 
# integers as the input of sumPrimes. 

# 2. We define function worker which 
# read an integer from the queue and call sumPrime. 

# 3. We next create 4 parallel python processes with worker as the target.
# note: for python 2 use Queue, for python3 use queue.


# In the code, ps is the new process created, worker is the name of the function 
# that the new process executes, and (arg1,arg2,...) is a 
# Python tuple specifying the input arguments of worker.


# Imports
import multiprocessing as mp
from queue import Empty 
import math
import os
import time


def primeQ(n):
    """return a boolean, is the input integer a prime?"""
    if n == 2 :
        return True
        
    max =  int( math.ceil( math.sqrt(n) ) )
    i = 2
    while i <= max :
        if n % i == 0 :
            return False
        i += 1
    return True
    
    
    
def sumPrimes(n):
    """return sum of all primes less than n """
    return sum( [ x for x in range(2,n) if primeQ(x) ] )




def worker(q):
    while True:
        try:
            x = q.get(block=False)
            print (sumPrimes(x))
        except Empty:
            break




start = time.time()
ncpus = 4 
my_q  = mp.Queue()
for i in range(10000, 200000, 10000):
    my_q.put(i)



procs=[mp.Process(target=worker, args=(my_q,))  for i in range(ncpus)]
for ps in procs:
    ps.start()
    
    
for ps in procs:
    ps.join()
    
    
mid  = time.time()

print ("now the serial part ")

for i in range(10000, 200000, 10000):
    print (sumPrimes(i))
    
ending = time.time()

print ("multiprocessing takes ", mid - start,      " seconds")
print ("single thread takes ",      ending - mid,  " seconds")

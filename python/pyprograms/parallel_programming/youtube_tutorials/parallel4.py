#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 04, 2016
#
# Info:
# 1. https://www.youtube.com/watch?v=s1SkCYMnfbY
#
#

# Imports
import math,random
from multiprocessing import Process,Queue
from os import getpid

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True
    

def process_main(q):
    while True:
        n = q.get()
        if n == 0:
            return True
        if is_prime(n):
            print(n)
    
if __name__ == '__main__':
    q = Queue()
    p = Process(target=process_main, args=(q,))
    p.start()
    for i in range(100):
        q.put(random.randint(0,1000))
    q.put(0)
    p.join()


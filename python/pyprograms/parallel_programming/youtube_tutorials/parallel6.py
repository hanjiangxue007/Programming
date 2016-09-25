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
from multiprocessing import Process,Manager
from time import sleep
from os import getpid

def counter(d):
    d[getpid()] = 0
    for i in range(10):
        sleep(.2)
        d[getpid()] += 1
    return 0
    

    
if __name__ == '__main__':
    with Manager() as m:
        d = m.dict()
        p1 = Process(target=counter, args=(d,))
        p2 = Process(target=counter, args=(d,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(d)



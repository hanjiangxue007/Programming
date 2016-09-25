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
from multiprocessing import Process,Value,Lock
from time import sleep

def counter(c,l):
    for i in range(10):
        sleep(.3)
        l.acquire()  # if acquire and release are commented, we get
        c.value += 1 # different answers, since process is not locked.
        l.release()  # lock makes program slow
	
    return 0
    

    
if __name__ == '__main__':
    v = Value('i',0)
    l = Lock()
    p1 = Process(target=counter, args=(v,l))
    p2 = Process(target=counter,args=(v,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(v.value)



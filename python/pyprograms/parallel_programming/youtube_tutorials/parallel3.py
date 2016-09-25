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
import os
from multiprocessing import Process,Pipe 
from time import sleep

def ponger(p,s):
    count = 0
    while count < 10:
        msg = p.recv()
        print('Process{0} got message: {1}'.format(os.getpid(),msg))
        sleep(1)
        p.send(s)
        count += 1
	
    
    
if __name__ == '__main__':
    parent,child = Pipe()
    proc = Process(target=ponger, args=(child,"ping"))
    proc.start()
    parent.send('pong')
    ponger(parent,'pong')
    proc.join()

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
from multiprocessing import Process 
from os import getpid

def prove_existence():
    print(getpid())
    
    
if __name__ == '__main__':
    p = Process(target=prove_existence, args=())
    p.start()
    p.join()
    p2 = Process(target=prove_existence, args=())
    p2.start()
    p2.join()

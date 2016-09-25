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
from multiprocessing import Pool

def start_function_for_processes(n):
    result_sent_back_to_parent = n*n
    return result_sent_back_to_parent
    
    
if __name__ == '__main__':
    with Pool(processes=5) as p:
        results = p.map(start_function_for_processes, range(200), chunksize=10)
    print(results)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 15, 2016
# Ref     : https://docs.python.org/2/library/timeit.html

# To check the time for running func1:
# python -mtimeit -s'import using_timeit' 'using_timeit.func1()'

def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

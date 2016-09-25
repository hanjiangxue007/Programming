#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 15, 2016
# Program : to compare two blocks of code or functions

# To check the time for running func1:
# python -mtimeit -s'import using_timeit' 'using_timeit.func1()'

# Imports
import timeit

start_time = timeit.default_timer()
def func1():
	for x in range(0,10000):
		x=x+1
	

	
func1()
print(timeit.default_timer() - start_time)


start_time = timeit.default_timer()
def func2():
	for x in range(0,10000):
		x=x+1
		

func2()
print(timeit.default_timer() - start_time)

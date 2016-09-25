#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 07, 2016
# Last update :
#
# Inputs      : none
#
# Outputs     :
#
# Info:
# 1. If we did not type argument, we can see help using this:
# python3 argsparse1.py -h
#

# Imports
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The Fibonacci number you wish to calculate.", type=int)

    args = parser.parse_args()

    result = fib(args.num)
    print("The " + str(args.num)+ "th fib number is " + str(result))

if __name__ == '__main__':
    Main()

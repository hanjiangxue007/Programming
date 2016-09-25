#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 07, 2016
# Last update :
#
# Inputs      : none
#
# Usage       : python3 argsparse_output_file.py 5
# Usage       : python3 argsparse_output_file.py 9 -o
#
# Info:
# 1.
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
    parser.add_argument("-o", "--output", help="Output the result to a file", action="store_true")

    args = parser.parse_args()

    result = fib(args.num)
    print("The " + str(args.num)+ "th fib number is " + str(result))

    if args.output:
        with open("fibonacci.txt","a") as f:
            print('Writing output to a file.')
            f.write(str(result) + '\n')

if __name__ == '__main__':
    Main()

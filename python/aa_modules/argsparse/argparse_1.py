#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 05, 2016
# Last update :
#
# Info: python argparse_1.py -h
#
# Imports
from __future__ import division, unicode_literals, print_function
import argparse

def main(a, b):
    """ Short script to add two numbers """
    return a + b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Add two numbers")
    parser.add_argument('-a',
                        help='First value',
                        type=float,
                        default=0)
    parser.add_argument('-b',
                        help='Second value',
                        type=float,
                        default=0)
    args = parser.parse_args()
    print(main(args.a, args.b))

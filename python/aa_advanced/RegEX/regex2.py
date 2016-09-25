#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 08, 2016
# Last update :
#
# Inputs      : none
#
# Outputs     :
#
# Info:
# 1.
#
# python3 regex2.py main code.txt

# Imports
import re
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='specify word to search for')
    parser.add_argument('fname', help='specify file to search')
    args = parser.parse_args()

    searchFile = open(args.fname)
    lineNum = 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word, line, re.M|re.I)
        if searchResult:
           print(str(lineNum) + ': ' + line)


if __name__ == '__main__':
    Main()

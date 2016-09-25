#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 22, 2016
# Ref       : https://stackoverflow.com/questions/3961265/get-line-number-of-certain-phrase-in-file-python 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# method 1


def get_line_number(phrase, file_name):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if phrase in line:
                return i




line_num = get_line_number('14.2000', 'input.txt')
print('{} {} {}'.format('line_num = ',line_num, ''))


line_num = get_line_number('0.532000', 'input.txt')
print('{} {} {}'.format('line_num = ',line_num, ''))






##=============================================================================
# method 2
def line_num_for_phrase_in_file(phrase, filename):
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if phrase in line:
                return i
    return -1


line_num = line_num_for_phrase_in_file('14.2000', 'input.txt')
print('{} {} {}'.format('\n\nline_num = ',line_num, ''))


line_num = line_num_for_phrase_in_file('0.532000', 'input.txt')
print('{} {} {}'.format('line_num = ',line_num, ''))


# method 3
print("\n")
#for n,line in enumerate(open("input.txt")):
    #if "14.20" in line: print (n+1)


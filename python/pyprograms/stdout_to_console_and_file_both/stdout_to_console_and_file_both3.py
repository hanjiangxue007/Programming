#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 12, 2016
 

# ./stdout_to_console_and_file_both3.py 2>&1 | tee output.txt

with open('out.txt', 'a') as f:
    print('hello world', file=f)

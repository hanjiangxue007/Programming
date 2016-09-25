#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
 # Date      : Jun 17, 2016


# Imports
from __future__ import print_function


with open('input.txt', 'r') as f:
    data = f.readlines()

comments_lines = 0
for line in data:
    if line.strip().startswith('#'):
        comments_lines += 1
    else:
        break

nfiles = 20
chunk_size = (len(data)-comments_lines)//nfiles

for i in range(nfiles):
    with open('output_{:02d}.txt'.format(i), 'w') as f:
        f.write(''.join(data[:comments_lines] + data[comments_lines+i*chunk_size:comments_lines+(i+1)*chunk_size]))
        if i == nfiles - 1 and len(data) > comments_lines+(i+1)*chunk_size:
            f.write(''.join(data[comments_lines+(i+1)*chunk_size:]))

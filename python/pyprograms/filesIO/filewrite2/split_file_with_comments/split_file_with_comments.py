#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# This program takes one input file, copies its comments to each of the
#    twenty splitted output files

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Store comments in this to use for all files
comments = []

# Create a new sub list for each of the 20 files
data = []
for _ in range(20):
    data.append([])

# Track line number
index = 0

# open input file
with open('input.txt', 'r') as fi:
    # fetch all lines at once so I can count them.
    lines = fi.readlines()

    # Loop to gather initial comments
    line = lines[index]
    while line.split()[0] == '#':
        comments.append(line)
        index += 1
        line = lines[index]

    # Calculate how many lines of data
    numdata = len(lines) - len(comments)

    for i in range(index, len(lines)):
        # Calculate which of the 20 files I'm working with
        filenum = (i - index) * 20 / numdata
        # Append line to appropriately tracked sub list
        data[filenum].append(lines[i])

for i in range(1, len(data) + 1):
    # Open output file
    with open('output{}.txt'.format(i), 'w') as fo:
        # Write comments
        for c in comments:
            fo.write(c)
        # Write data
        for line in data[i-1]:
            fo.write(line)

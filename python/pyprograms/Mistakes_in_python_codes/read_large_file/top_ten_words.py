#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 08, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
# Ref: http://carl.cs.indiana.edu/cnets-howto/howtos/mistakes.html

# Imports
import pprint

# good way
counts = {}

infile = 'large_text.txt'
with open(infile,'r')as f:
    for line in f:
        for word in line.split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
                
counts = sorted(counts.items(), key=lambda k : k[1], reverse=True)
pprint.pprint(counts[:10])

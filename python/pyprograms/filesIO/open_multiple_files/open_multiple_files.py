#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

    
try:
    with open('in.txt', 'r') as fi, open ('out.txt', 'w') as fo:
        print('hello', file = fo)

except IOError as e:
    print ('Operation failed: %s' % e.strerror)

    

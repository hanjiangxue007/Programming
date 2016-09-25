#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os,shutil


# using os.remove
filename = 'file.txt'
if os.path.isfile(filename):
    os.remove(filename)


# use try except method
# this avoids TOCTTOU bug
try:
    os.remove(filename)
except OSError:
    pass

# using ternary operation:
os.remove(filename) if os.path.isfile(filename) else None

# remove a dir
# https://stackoverflow.com/questions/1557351/python-delete-non-empty-dir
shutil.rmtree('tmp',ignore_errors=True)

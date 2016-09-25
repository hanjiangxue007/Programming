#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://stackoverflow.com/questions/20607661/append-contents-from-one-file-to-another-with-newline-separation 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os,shutil


with open("file1.txt",'rb') as fin1, \
     open("file2.txt",'rb') as fin2,  \
     open("file3.txt",'wb') as fout:
    shutil.copyfileobj(fin1, fout)
    fin1.seek(-len(os.linesep), 2)
    if fin1.read() != os.linesep:
            fout.write(os.linesep)
    shutil.copyfileobj(fin2, fout)




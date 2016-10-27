#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-18-2016 Tue
# Last update :
#
# Ref: http://nullege.com/codes/search/matplotlib.cbook.get_sample_data
#
# Imports
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mimage
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook


print(matplotlib.__version__)  # 1.5.1
fname = cbook.get_sample_data('msft.csv', asfileobj=False)

with open(fname,'r') as f:
    read_data = f.read()


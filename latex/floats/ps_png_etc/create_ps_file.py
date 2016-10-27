#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-17-2016 Mon
# Last update :
#
#
# Imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3])
fig.savefig('images/test.ps')
fig.savefig('images/test.eps')
fig.savefig('images/test.png')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 28, 2016
# Topic   : OverflowError: Allocated too many blocks
# Note    : python --version ==> Python 2.7.10
# Note    : lsb_release -a   ==> ubuntu 15.10

# Imports
import numpy as np
import matplotlib.pyplot as plt


# try
import matplotlib as mpl
#mpl.rcParams['backend'] = 'Qt4Agg'
mpl.rcParams['agg.path.chunksize'] = 20000


# Get the backend
print(plt.get_backend())  # Qt4Agg


# subplots
fig, ax = plt.subplots()

# x = r/M values
x = np.arange(0.001, 25.0, 0.1)
A = 4.3
y = np.array( (-1.0/x) + (0.5*A*A/(x**2)) - (A*A/(x**3)) )

# Plots
plt.plot(x,y,color='k')

# Set axes limits
plt.ylim(-0.04,0.06)

# Fill the color
plt.fill_between(x, -0.04, y, color='darkgray', alpha=.5)

# Show the plot
plt.show()

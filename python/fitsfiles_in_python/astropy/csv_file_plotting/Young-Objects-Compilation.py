#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

# Imports
from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii



tbl = ascii.read("Young-Objects-Compilation.csv")
#print(tbl.colnames)
# What happened? The column names are just col1, col2, etc., the default names
# if ascii.read() is unable to parse out column names. We know it failed to
# read the column names, but also notice that the first row of data are
# strings -- something else went wrong!

print("\n")
#print(tbl[0])

# A few things are causing problems here. First, there are two header lines in
# the file and the header lines are not denoted by comment characters.
# The first line is actually some meta data that we don't care about,
# so we want to skip it. We can get around this problem by specifying the
# header_start keyword to the ascii.read() function. This keyword argument
# specifies the index of the row in the text file to read the column names from:





tbl = ascii.read("Young-Objects-Compilation.csv", header_start=1)
print(tbl.colnames)

# Great -- now the columns have the correct names, but there is still a problem:
# all of the columns have string data types, and the column names are
# still included as a row in the table. This is because by default the data
# are assumed to start on the second row (index=1). We can specify data_start=2
# to tell the reader that the data in this file actually start on the 3rd
# (index=2) row:



tbl = ascii.read("Young-Objects-Compilation.csv", header_start=1, data_start=2)
# Some of the columns have missing data, for example, some of the RA values
# are missing (denoted by -- when printed):
print("\n")
print(tbl['RA'])


# This is called a Masked column because some missing values are masked out
# upon display. If we want to use this numeric data, we have to tell astropy
# what to fill the missing values with. We can do this with the .filled() method.
# For example, to fill all of the missing values with NaN's:
print("\n")
print(tbl['RA'].filled(np.nan))


# Let's recap what we've done so far, then make some plots with the data.
# Our data file has an extra line above the column names, so we use
# the header_start keyword to tell it to start from line 1 instead of
# line 0 (remember Python is 0-indexed!). We then used had to specify that
# the data starts on line 2 using the data_start keyword.
# Finally, we note some columns have missing values.

data = ascii.read("Young-Objects-Compilation.csv", header_start=1, data_start=2)

# Now that we have our data loaded, let's plot a color-magnitude diagram.
# Here we simply make a scatter plot of the J-K color on the x-axis against the
# J magnitude on the y-axis. We use a trick to flip the y-axis
# plt.ylim(reversed(plt.ylim())). Called with no arguments, plt.ylim() will
# return a tuple with the axis bounds, e.g. (0,10). Calling the function
# with arguments will set the limits of the axis, so we simply set the limits
# to be the reverse of whatever they were before. Using this pylab-style
# plotting is convenient for making quick plots and interactive use,
# but is not great if you need more control over your figures.

plt.scatter(data["Jmag"] - data["Kmag"], data["Jmag"]) # plot J-K vs. J
plt.ylim(reversed(plt.ylim())) # flip the y-axis
plt.xlabel("$J-K_s$", fontsize=20)
plt.ylabel("$J$", fontsize=20)
#plt.show()





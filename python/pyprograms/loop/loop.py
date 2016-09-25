#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 24, 2016

# example 1
for letter in "Codecademy":
    print letter

# example 2
for x in range(0, 3):
    print "We're on time %d" % (x)


# Creating y labels from -0.075 to 0.1 including
ylabels = []
ylabel = -0.075

while ylabel < 0.1001:
    ylabels.append(ylabel)
    ylabel +=  0.025

print(ylabels)


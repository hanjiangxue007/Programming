#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct 06, 2016
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function
from visual.graph import * # import graphing features
from numpy import arange, cos, exp

funct1 = gcurve(color=color.cyan) # a connected curve object

for x in arange(0., 8.1, 0.1): # x goes from 0 to 8
    funct1.plot(pos=(x,5.*cos(2.*x)*exp(-0.2*x))) # plot

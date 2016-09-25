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
# Ref : http://nealhughes.net/cython1/

# Imports
from math import exp
import numpy as np

def rbf_network(X, beta, theta):

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y



##===================================================================

# make some data
D = 5
N = 1000
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

# go to ipython and %paste and run below line
# %timeit rbf_network(X, beta, theta)

# answer: 7.67 sec

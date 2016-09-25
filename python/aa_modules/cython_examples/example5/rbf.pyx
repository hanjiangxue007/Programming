#cython: boundscheck=False, wraparound=False, nonecheck=False


# be very careful to use boundscheck=False,etc,
# it may give segfault instead of Error log for python program!


from libc.math cimport exp 
#from math import exp # this is slower
import numpy as np

def rbf_network(double[:, :] X,  double[:] beta, double theta):

    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef double[:] Y = np.zeros(N)
    cdef int i, j, d
    cdef double r = 0

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y



# to compile: python setup.py build_ext --inplace
# gives: rbf.c and rbf.so

# test from ipython:

#     first copy some data to test:

#import numpy as np
#D = 5
#N = 1000
#X = np.array([np.random.rand(N) for d in range(D)]).T
#beta = np.random.rand(N)
#theta = 10


# then use timeit:
#     from rbf import rbf_network
#     %timeit rbf_network(X, beta, theta)


# comparison: 
# vanilla python : 7.67 seconds = 7670 ms
# cython         : 247 ms
# improved_cython: 59.7 ms

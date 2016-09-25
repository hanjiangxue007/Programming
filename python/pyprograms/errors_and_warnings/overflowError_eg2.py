#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 28, 2016
# Topic   : OverflowError: Allocated too many blocks
# Note    : python --version ==> Python 2.7.10
# Note    : lsb_release -a   ==> ubuntu 15.10

# Imports

### problem
import matplotlib.pyplot as plt
import numpy as np

signal = [round(np.random.random() * 100) for i in xrange(0, 1000000)]
plt.plot(signal)
plt.show()


## solution
#import random
#import pylab as plt
#signal = [round(random.random() * 100) for i in xrange(0, 1000000)]
#plt.plot(signal, '.')
#plt.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import numpy as np
from StringIO import StringIO

test = "a,1,2\nb,3,4"
a = np.genfromtxt(StringIO(test), delimiter=",", dtype=None)
print (a)


b = np.genfromtxt(StringIO(test), delimiter=",", dtype=("|S10", int, float))
print(b)

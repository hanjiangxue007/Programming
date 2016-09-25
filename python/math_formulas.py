#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 14, 2016
# Last update :
#

# Imports
import numpy as np
from numpy import sqrt,log,log10,sin,cos,tan,exp
from scipy.constants import k # boltzmann const
#from scipy.constants import pi,hbar,c,e,epsilon_0,m_e,m_p





def formula():

    # variables
    a = 1.86e12
    b = 0.051
    c = 3
    d = 365*86400
    e = 0
    f = 0
    g = 0
    m = 0
    r = 0
    l = 0
    m = 0
    n = 0
    p = 0
    q = 0


    return a*b/c/d
if __name__ == '__main__':
    y= formula()
    print('{} {:fMa} {}'.format('y = ',y, ''))


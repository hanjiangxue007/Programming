#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

# Imports
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as PLT
import numpy as NP

fig = PLT.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = NP.random.randint(1, 10, 10)
ypos = NP.random.randint(1, 10, 10)
num_elements = 10
zpos = NP.zeros(num_elements)
dx = NP.ones(10)
dy = NP.ones(10)
dz = NP.random.randint(1, 5, 10)

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#8E4585')
PLT.show()

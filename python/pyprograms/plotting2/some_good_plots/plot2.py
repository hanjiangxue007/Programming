#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 09, 2016
# Last update :
#
# Depends     : none
#
# Outputs     :
#
# Info:
# to open fig from terminal
# eog example01.png &
# “eog” stands for Eye of Gnome and is the default graphics
# viewer for the Gnome desktop environment
#
#

# Imports
import matplotlib.pyplot as pyplot
import numpy as np
from numpy import pi

x = np.linspace(-2*pi, 2*pi, 100)
y = np.sin(0.25*x)

# plot this
pyplot.plot(x,y)

# axis
pyplot.axis([-1.5, 1.5, -1.5, 1.5])

# ticks
pyplot.xticks([0.25*k for k in range(-4,5)])
pyplot.yticks([-0.9, -0.4, 0.0, 0.3, 0.6, 0.85])

pyplot.yticks([-0.9, -0.4, 0.0, 0.3, 0.6, 0.85],
 ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta'])

# title
pyplot.title('y = x cubed\nfrom x=-1 to x=1')
pyplot.title('$y = x^{3}$\n$-1<x<1$')

# labels
pyplot.xlabel('$-1<x<1$')
pyplot.ylabel('$y=x^{3}$')
pyplot.ylabel('$y=x^{3}$', rotation='horizontal')

# legends
pyplot.line = pyplot.plot(x,y, label='x cubed')
pyplot.legend()

pyplot.line = pyplot.plot(x,y, label='x cubed')
pyplot.legend(loc='upper left')
pyplot.legend(title='The legend')

# line properties
pyplot.plot(x,y, color='green', linestyle='dashed',
linewidth=5.0)




#pyplot.savefig('example01.png')
pyplot.show()


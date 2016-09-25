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
# 1.
#
#

# Imports
import numpy as np
import matplotlib.pyplot as plt

plt.clf() #Clear the current figure (prevents multiple labels)

labelfont = {
        'family' : 'sans-serif',  # (cursive, fantasy, monospace, serif)
        'color'  : 'black',       # html hex or colour name
        'weight' : 'normal',      # (normal, bold, bolder, lighter)
        'size'   : 14,            # default value:12
        }

titlefont = {
        'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 16,
        }

pi = np.pi
x = np.linspace(-2*pi, 2*pi, 100)
f1 = np.sin(0.25*x)
f2 = np.cos(x)

plt.plot(x, f1,
         'darkgreen',                       # colour
         linestyle='--',                    # line style
         linewidth=3,                       # line width
         label='$0.25 \cdot \sin(x)$')      # plot label

plt.plot(x, f2,
         'darkmagenta',
         linestyle='-',
         linewidth=3,
         label='$\cos(x)$')

axes = plt.gca()
axes.set_xlim([-2*pi, 2*pi])            # x-axis bounds
axes.set_ylim([-1.5, 1.5])              # y-axis bounds

legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

plt.title('Trigonometric functions', fontdict=titlefont)
plt.xlabel('Angle (in radians)', fontdict=labelfont)
plt.ylabel('Function', fontdict=labelfont)

plt.subplots_adjust(left=0.15)        # prevents overlapping of the y label

plt.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Mar 28, 2016
# Ref     : http://web.stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html#styling-figures-with-axes-style-and-set-style

# Imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(sum(map(ord, "aesthetics")))

#Let’s define a simple function to plot some offset sine waves, which will help
#us see the different stylistic parameters we can tweak.

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.show()

#sinplot()

# To switch to seaborn defaults, simply import the package.

import seaborn as sns
sinplot()



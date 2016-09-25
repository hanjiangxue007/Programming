#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/17141558/how-to-sort-a-dataframe-in-python-pandas-by-two-or-more-columns


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame(np.random.randint(1, 5, (10,2)), columns=['a','b'])
df1 = df1.sort_values(['a', 'b'], ascending=[True, False])
print(df1)

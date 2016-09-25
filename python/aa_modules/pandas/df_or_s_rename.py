#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



s = pd.Series([1, 2, 3])
print(s)

s = s.rename("my_name") # scalar, changes Series.name
print("\n")
print(s)




s = s.rename(lambda x: x ** 2)  # function, changes labels
print(s)
print("\n")


s = s.rename({1: 3, 2: 5})  # mapping, changes labels
print(s)
print("\n")



df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)
print("\n")



#df.rename(2)
#...
#TypeError: 'int' object is not callable

# rename method 1
#df = df.rename(index=str, columns={"A": "apple", "B": "ball"})
#print(df)


## rename method 2
#old_names = ['A', 'B','C']
#new_names = ['a', 'b','c']
#df.rename(columns=dict(zip(old_names, new_names)), inplace=True)
#print('{} {} {} {}'.format('\nrename columns\ndf = \n', df,'',''))

# rename method 3
#df.rename(columns = {'A':'Apple'}, inplace = True)
#print(df)

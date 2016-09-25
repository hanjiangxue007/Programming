#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : https://stackoverflow.com/questions/24284342/insert-a-row-to-pandas-dataframe 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s1 = pd.Series([5, 6, 7])
s2 = pd.Series([7, 8, 9])

df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])
print(df)


# adding a row at the top
df = pd.DataFrame(np.array([[2, 3, 4]]), columns=['A', 'B', 'C']).append(df, ignore_index=True)
print("\n")
print(df)


# method 2
df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])
df.loc[-1] = [2, 3, 4]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index
print("\n")
print(df)


# method 3
df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])
df2 = pd.DataFrame([[2,3,4]],columns=['A','B','C'])
df = pd.concat([df2,df])
print("\n")
print(df)


# adding a row at the bottom
df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])
df2 = pd.DataFrame(np.array([[20, 30, 40]]), columns=['A', 'B', 'C'])
df = df.append(df2, ignore_index=True)
print("\n")
print(df)


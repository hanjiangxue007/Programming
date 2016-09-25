#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://pythonforengineers.com/introduction-to-pandas/

# Imports
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('wages_hours.csv', sep='\t')
print(data.head())

# only age and rate
print("\n")
data2 = data[["AGE", "RATE"]]
print(data2.head())

# sorting AGE using sort_values
print("\n")
data_sorted = data2.sort_values(['AGE'], ascending=[True])
print(data_sorted.head())

# reset index to AGE
print("\n")
data_sorted.set_index("AGE",inplace=True)
print(data_sorted.head())

# plot
data_sorted.plot()
plt.show()

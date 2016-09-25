#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 20, 2016
# Ref       : https://stackoverflow.com/questions/21065938/read-a-single-column-of-a-csv-and-store-in-an-array 

# Imports
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("foo.csv")

date = df['date']  # as a Series
date2 = df['date'].values  # as a numpy array

print(df)
print("\n")
print(date)


# method 2
date = pd.read_csv("foo.csv", sep=',', usecols=['date'], squeeze=True)

print("\n")
print(date)
print("\n")
print(date.values)

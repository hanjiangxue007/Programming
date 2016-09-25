#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016


# Imports
import pandas as pd

data = pd.read_csv('whitespace.csv', delim_whitespace=True,skiprows=0)
print(data)

# you can use regex as the delimiter:
print("\n")
data = pd.read_csv("whitespace.csv", header=None, delimiter=r"\s+")
print(data)




# skip initial spaces
print("\n")
data = pd.read_csv('whitespace.csv', delim_whitespace=True,skiprows=0,
                    skipinitialspace=True,header=None)
print(data)

# print all lines
print("\n")
for line in open("whitespace.csv"):
    print repr(line)


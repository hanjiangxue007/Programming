#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(range(-3, 4))
print(s)

s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print("\n")
print(s)

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df = pd.DataFrame(np.linspace(-10,13,num=24).reshape(6,4), index=dates, columns=list('ABCD'))
print("\n")
print(df)


df3 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]})

print("\n")
print(df3)

# example
n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print("\n")
print(df)


# example
n = 10
df = pd.DataFrame( np.random.randint(n, size=(n,3)) , columns=list('abc'))
print("\n")
print(df)

# example
df = pd.DataFrame({ 'a': list('aabbccddeeff'),
                    'b': list('aaaabbbbcccc'),
                    'c': np.random.randint(5, size=12),
                    'd': np.random.randint(9, size=12)  })
print("\n")
print(df)


# example
s1 = pd.Series([5, 6, 7])
s2 = pd.Series([7, 8, 9])

df = pd.DataFrame([list(s1), list(s2)],  columns =  ["A", "B", "C"])
# better way is below:
df = pd.DataFrame([s1.values, s2.values],  columns =  ["A", "B", "C"])

print("\n")
print(df)

#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-advanced

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# You can also use the levels of a DataFrame with a MultiIndex as if they were columns in the frame:
n = 10
colors = np.random.choice(  ['red', 'green'], size = n   )
foods  = np.random.choice(  ['eggs', 'ham'] , size =n    )

print("\n")
print(colors)
print("\n")
print(foods)

index = pd.MultiIndex.from_arrays(  [colors,foods], names = ['color', 'food']        )
df = pd.DataFrame( np.random.randn(n,2),   index = index) # two random columns with given index
print("\n")
print(df)


dfq = df.query('  color == "red"   ')
print("\n")
print(dfq)

##=============================================================================
# If the levels of the MultiIndex are unnamed, you can refer to them using special names:

df.index.names = [None, None]
print("\nindex.name made None \n")
print(df)

df1 = df.query( 'ilevel_0 == "red" ')
print("\nThe convention is ilevel_0, which means “index level 0” for the 0th level of the index.\n")
print(df1)

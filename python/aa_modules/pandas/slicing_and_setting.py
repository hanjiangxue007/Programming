#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 
# Ref       : https://stackoverflow.com/questions/12307099/modifying-a-subset-of-rows-in-a-pandas-dataframe

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({ 'A' : [ 0, 2,3,4,5],
                    'B' : [ 10, 20, 30,40,50],
                    'C' : [ 100, 200, 300,400,500]

                   })


# df.ix[selection criteria, columns I want] = value

# the df.A==0 expression creates a boolean series that indexes the rows, 'B' selects the column. 
df.ix[df.A==0, 'B'] = np.nan
print(df)



#df.ix[ (df['A'] >=  2) & (df['A'] <=  4) , ['B','C'] ] = 0

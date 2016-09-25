#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

# Imports
import numpy as np
import pandas as pd


df = pd.read_csv('mariano-rivera.csv')
dfhead = df.head()
#print(dfhead)

##=============================================================================
cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('peyton-passing-TDs-2012.csv', sep=',', header=None,
                         names=cols)
print(no_headers.head())

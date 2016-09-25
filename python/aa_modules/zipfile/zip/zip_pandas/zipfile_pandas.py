#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
 

# Imports
import pandas as pd
import zipfile

zf = zipfile.ZipFile('First.csv.zip') # having First.csv zipped file.
df = pd.read_csv(zf.open('First.csv'))

print(df)

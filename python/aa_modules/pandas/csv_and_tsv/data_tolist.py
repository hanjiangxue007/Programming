#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python

# Imports
import pandas as pd



infile = 'df_tolist.csv'
colnames = ['year', 'name', 'city', 'latitude', 'longitude']
df = pd.read_csv(infile, names=colnames)

# convert data_frame to list
names = df.name.tolist()
latitude = df.latitude.tolist()
longitude = df.longitude.tolist()

print(names)

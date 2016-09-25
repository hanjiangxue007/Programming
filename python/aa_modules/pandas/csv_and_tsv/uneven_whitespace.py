#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://stackoverflow.com/questions/22809061/read-space-separated-data-with-pandas

# Regex     : https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/

# Imports
import pandas as pd

# df = pd.read_csv(filename, sep=' ',header=None)
# This specifies the separator as a single space, because your csvs can
# have spaces or tabs you can pass a regular expression to the sep param like so:

filename = 'uneven_whitespace.csv'
df = pd.read_csv(filename, sep='\s+',header=None) # or, sep=r"\s+"
print(df)

# This defines separator as being one single white space or more, there is a
# handy cheatsheet that lists regular expressions.



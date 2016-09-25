#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016
# Ref       : https://docs.python.org/3/library/gzip.html

# Imports
import gzip
import shutil


with open('a.txt', 'rb') as f_in:
    with gzip.open('a.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016
# Ref       : http://www.dotnetperls.com/compression-python 

# Imports
import gzip

# Use open method.
with gzip.open("a.gz", "rb") as f:
    # Read in string.
    content = f.read()

    # Print length.
    print(len(content))



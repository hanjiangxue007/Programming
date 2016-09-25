#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016
# Ref       : https://docs.python.org/3/library/gzip.html

# Imports
import gzip

content = b"Lots of content here"
with gzip.open('tmp2.txt.gz', 'wb') as f:
    f.write(content)

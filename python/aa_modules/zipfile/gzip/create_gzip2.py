#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016
# Ref       : http://www.dotnetperls.com/compression-python 

# Imports
import gzip

# Open source file.
with open("a.txt", "rb") as file_in:
    # Open output file.
    with gzip.open("a.gz", "wb") as file_out:
        # Write output.
        file_out.writelines(file_in)


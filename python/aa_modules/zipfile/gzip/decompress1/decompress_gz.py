#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016

# Imports
import gzip
import os

infile = r"source/a.fits.gz"
outfile = infile[:-3]



with gzip.open(infile,"rb") as inzip, open(outfile,"wb") as outzip:

    zipdata = inzip.read()
    outzip.write(zipdata)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016

# Imports
import gzip
import os

indir = r'./source/'
infile = r"a.fits.gz"

outdir = r'./dest/'
outfile = outdir + infile[:-3]



with gzip.open(indir + infile,"rb") as inzip, open(outfile,"wb") as outzip:

    zipdata = inzip.read()
    outzip.write(zipdata)




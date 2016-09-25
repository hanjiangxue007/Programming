#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016

# Imports
import gzip
import glob
import os

indir = 'source'
outdir = r'dest'

for infile in glob.glob("%s/*.gz" % indir):
    if not os.path.isdir(infile):
        with gzip.open(infile, 'rb') as inzip:
            zipdata = inzip.read()

        # outfile       
        outfile = outdir + "/" + os.path.basename(infile)[:-3]
        print('{} {} {}'.format('\ninfile :',infile, ''))
        print('{} {} {}'.format('outfile :',outfile, ''))

        # store uncompressed file data from 'zipdata' variable
        with open(outfile, 'wb') as f:
            f.write(zipdata)

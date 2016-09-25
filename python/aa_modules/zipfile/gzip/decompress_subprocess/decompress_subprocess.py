#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 18, 2016

# Imports
import os,glob,subprocess,shutil

indir = r'source'
infile = r"a.fits.gz"

outdir = r'dest'
outfile = outdir + infile[:-3]



for file in glob.glob(indir + "/*.gz"):
    if os.path.isdir(file) == False:
        shutil.copy(file, outdir)
        
        # uncompress the file
        subprocess.call(["gunzip", outdir + "/" + os.path.basename(file)])


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 12, 2016
# Last update :
#

# Imports
from pdfrw import PdfReader, PdfWriter

output = PdfWriter()

for p in PdfReader('source.pdf').pages:
  if p.Contents is not None:
    output.addpage(p)

output.write('newfile.pdf')

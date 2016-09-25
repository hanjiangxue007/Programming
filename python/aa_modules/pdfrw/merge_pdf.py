#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 12, 2016
# Last update :
#
# Ref: https://www.binpress.com/tutorial/manipulating-pdfs-with-python/171
#

# Imports
import os
from pdfrw import PdfReader, PdfWriter

writer = PdfWriter()

files = [x for x in os.listdir('mypdfs') if x.endswith('.pdf')]
for fname in sorted(files):
  writer.addpages(PdfReader(os.path.join('mypdfs', fname)).pages)

writer.write("output.pdf")

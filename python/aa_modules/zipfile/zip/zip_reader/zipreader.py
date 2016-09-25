#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
 

# Imports
import zipfile

def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    for finfo in zfile.infolist():
        ifile = zfile.open(finfo)
        line_list = ifile.readlines()
        print (line_list)


filepath = 'a.txt.zip'
read_zip_file(filepath)

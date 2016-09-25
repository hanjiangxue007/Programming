#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://stackoverflow.com/questions/19371860/python-open-file-from-zip-without-temporary-extracting-it

# Imports
import zipfile


##=============================================================================
archive = zipfile.ZipFile('example.zip', 'r')
imgdata = archive.read('a.txt')
print('{} {} {}'.format('type imgdata: ',type(imgdata), ''))
print('{} {} {}'.format('imgdata: ',imgdata, ''))
##=============================================================================


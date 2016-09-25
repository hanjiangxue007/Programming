#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://pymotw.com/2/zipfile/ 

# Imports
import zipfile


##=============================================================================
z = zipfile.ZipFile("example.zip", "r")

for filename in z.namelist(  ):
    print ('File:', filename,)
    bytes = z.read(filename)
    print ('has',len(bytes),'bytes\n')
##=============================================================================


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://pymotw.com/2/zipfile/ 

# Imports
import zipfile


## Extracting Archived Files From a ZIP Archive
## To access the data from an archive member, use the read() method,
##  passing the member’s name.

zf = zipfile.ZipFile('example.zip')
for filename in [ 'a.txt', 'notthere.txt' ]:
    try:
        data = zf.read(filename)
    except KeyError:
        print ('ERROR: Did not find %s in zip file' % filename)
    else:
        print (filename, ':')
        print (repr(data))
    print ("")

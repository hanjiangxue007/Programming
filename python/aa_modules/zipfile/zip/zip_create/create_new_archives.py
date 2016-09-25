#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://pymotw.com/2/zipfile/ 

# Imports
import zipfile


try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
          }

print ('creating archive')
zf = zipfile.ZipFile('zipfile_write_compression.zip', mode='w')
try:
    print ('adding a.txt with compression mode', modes[compression])
    zf.write('a.txt', compress_type=compression)
finally:
    print ('closing')
    zf.close()

print("")


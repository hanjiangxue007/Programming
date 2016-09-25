#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://stackoverflow.com/questions/21075999/selective-extracting-and-opening-for-zipfile-in-python?rq=1

# Imports
import os
import zipfile


wanted = {'a.txt', 'b.txt','nothere.txt'}  # use a set, it's faster for testing membership
with zipfile.ZipFile('foobar.zip','r') as inzipfile:
    for infile in (name for name in inzipfile.namelist() if name[-1] != '/'):
        if os.path.split(infile)[1] in wanted:
          print (inzipfile.open(infile,'r').read())


##=============================================================================
## The only way I can think of to check if all the [file] members of an archive
# can be opened, is to actually try doing it to each one:

def check_files(zipfilename):
    """ Check and see if all members of a .zip archive can be opened.
        Beware of vacuous truth - all members of an empty archive can be opened
    """
    def can_open(archive, membername):
        try:
            archive.open(membername, 'r')  # return value ignored
        except (RuntimeError, zipfile.BadZipfile, zipfile.LargeZipFile):
            return False
        return True

    with zipfile.ZipFile(zipfilename, 'r') as archive:
        return all(can_open(archive, membername)
                    for membername in (
                        name for name in archive.namelist() if name[-1] != '/'))


a = check_files('foobar.zip')
print('{} {} {}'.format('\nAll members of Archive can be opened: ',a, ''))

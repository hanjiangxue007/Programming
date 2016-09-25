#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://stackoverflow.com/questions/3451111/unzipping-files-in-python?rq=1

# Imports
import os,shutil
import io
import zipfile

def extract(filename):
    z = zipfile.ZipFile(filename)
    for f in z.namelist():

        print('{} {} {}'.format('extracting zipfile: ',f, ''))
        
        # get directory name from file
        dirname = os.path.splitext(f)[0]
         
        # create new directory
        shutil.rmtree(dirname,ignore_errors=True)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

              
        # read inner zip file into bytes buffer 
        content = io.BytesIO(z.read(f))
        inner_zip = zipfile.ZipFile(content)
        inner_zip.extractall(dirname)


extract("two_zipped_files.zip")


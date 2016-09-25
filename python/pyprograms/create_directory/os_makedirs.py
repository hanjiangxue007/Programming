#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 01, 2016
# Last update : 

# Inputs      : none
# Outputs     : tmp_folder

# Info:
# 1. This program creates an empty folder in given path, recursively
#

# Imports
import os,sys,shutil

# outfolder
outfolder = 'tmp_folder2/a/b/c'

if not os.path.exists(outfolder):
    os.makedirs(outfolder)
    print('{} {} {}'.format('folder created : ',outfolder, ''))


# delete non empty directory
if os.path.exists(outfolder):
    shutil.rmtree(outfolder)

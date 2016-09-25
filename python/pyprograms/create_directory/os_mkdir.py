#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 01, 2016
# Last update : 

# Inputs      : none
# Outputs     : tmp_folder

# Info:
# 1. This program creates an empty folder in given path, non_recursively
#

# Imports
import os, sys

# outfolder
outfolder = 'tmp_folder'  # can not create tmp_folder/a/b



if os.path.exists(outfolder):
    print('{} {} {}'.format('folder already exists : ',outfolder, ''))
    
if not os.path.exists(outfolder):
    os.mkdir(outfolder)
    print('{} {} {}'.format('folder created : ',outfolder, ''))


# write a file inside this
outfile = outfolder + '/a.txt'
with open (outfile, 'w' ) as fout:
    fout.write('hello')


## to use os.rmdir, we should delete all the files inside it
#if os.path.exists(outfile):
    #os.remove(outfile)     

# to remove empty directory
#if os.path.exists(outfolder):
    #os.rmdir(outfolder)

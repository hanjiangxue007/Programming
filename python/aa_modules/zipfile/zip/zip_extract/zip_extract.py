#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jul 11, 2016
# Ref       : https://stackoverflow.com/questions/3451111/unzipping-files-in-python?rq=1

# Imports
import zipfile

zippedfile = "two_zipped_files.zip"
zippedfile = "example.zip"
with zipfile.ZipFile(zippedfile,"r") as zip_ref:
    zip_ref.extractall(".")

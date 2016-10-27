#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-10-2016 Mon
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function


def pdf_from_images(indir,outpdf='output.pdf'):
    # imports
    from natsort import natsorted
    import os,subprocess

    #indir = 'images'
    #outpdf  = 'output.pdf'

    files = [x for x in os.listdir(indir) if x.endswith('.jpg')]
    files = natsorted(files)
    files = [indir + '/' + x for x in files]
    images = ' '.join(map(str, files))

    convert = 'convert -rotate 90 -compress jpeg -quality 75'
    cmd     = convert + ' ' + images + ' ' + outpdf

    print("\nCreating :", outpdf, "")
    subprocess.call(cmd,shell=True)

if __name__ == '__main__':
    indir  = 'images'
    outpdf = 'output.pdf'
    pdf_from_images(indir,outpdf)

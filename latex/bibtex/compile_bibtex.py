#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2016
# Last update : 
#
# Inputs      : 1. tex file
#               2. bib file
#
# Outputs     : 
#
# Info:
# 1. compiles latex with bibtex.
#
#

# Imports
import subprocess, sys,os

commands = [
    ['pdflatex', sys.argv[1] + '.tex'],
    ['bibtex', sys.argv[1] + '.aux'],
    ['pdflatex', sys.argv[1] + '.tex'],
    ['pdflatex', sys.argv[1] + '.tex']
]

for c in commands:
    subprocess.call(c)
    
# delete additional files
extensions = ['.aux', '.bbl', '.blg', '.bob', '.log', '.out']
for i in range(len(extensions)):
    
    fl = sys.argv[1] + extensions[i]
    if os.path.exists(fl):
        os.remove(fl)
        print('{} {} {}'.format('deleting: ',fl, ''))
        
## open the pdf
subprocess.call(['xdg-open', sys.argv[1] + '.pdf'])

# delete further files if exist
if os.path.exists('texput.log'):
    os.remove('texput.log')
    print('deleting: texput.log')

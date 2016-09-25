#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 29, 2016
# Ref       : https://stackoverflow.com/questions/22698754/subprocess-calls-are-they-done-in-parallel 

# Imports
import subprocess


nfiles = 5
for i in range(nfiles):

    # command    
    command = r'touch ' + 'junk_{:d}.txt'.format(i)

    # run the program
    subprocess.Popen(command,shell=True)


# note: subprocess.call is not parallized as same as subprocess.Popen("some-program").wait()

command = r'echo "hello"'
output, stderr = subprocess.Popen(command,shell=1).communicate()

print(output)  # None
print(stderr)  # None

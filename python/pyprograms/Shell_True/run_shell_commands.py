#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 24, 2016
# Ref       : https://stackoverflow.com/questions/89228/calling-an-external-command-in-python 

# Imports
from __future__ import print_function
import subprocess
import os


# using subprocess
#command = ["ls", "-l"]
command = ["echo", "subprocess call"]
subprocess.call(command,shell=False)

# eg2
a = subprocess.Popen("echo subprocess Popen", shell=True, stdout=subprocess.PIPE).stdout.read()
print(a)

# eg3
return_code = subprocess.call("echo Hello World", shell=True)
print('{} {} {}'.format('return code = ',return_code, ''))

# Command with shell expansion
subprocess.call('echo $HOME', shell=True)












# using os
# os.system is OK, but kind of dated. It's also not very secure.
print("\n")
cmd = 'echo \'os.system\''
os.system(cmd)




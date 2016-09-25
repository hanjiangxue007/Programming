#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 24, 2016
# Ref       : https://stackoverflow.com/questions/17742789/running-multiple-bash-commands-with-subprocess


import subprocess
from subprocess import Popen, PIPE, STDOUT


commands = '''
echo "a"
echo "b"
echo "c"
echo "d"
'''

subprocess.call(commands, shell=True)




##
## 
###=============================================================================
#def subprocess_cmd(command):
    #process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    #proc_stdout = process.communicate()[0].strip()
    #print (proc_stdout)

#subprocess_cmd('echo a; echo b')


###
###
###=============================================================================
#print('{} {} {}'.format('\n\nmethod 2:\n','', ''))
#commands = '''
#echo "a"
#echo "b"
#echo "c"
#echo "d"
#'''

#process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#out, err = process.communicate(commands)
#print (out)











##
## parallel method
###=============================================================================
##from subprocess import Popen
#print('{} {} {}'.format('\nparallel methods','', ''))

## run commands in parallel
#processes = [Popen("echo {i:d}; sleep 2; echo {i:d}".format(i=i), shell=True)
             #for i in range(5)]
             
## collect statuses
#exitcodes = [p.wait() for p in processes]



## write output log
##from subprocess import Popen, PIPE, STDOUT

#cmd1 = 'echo "hello world"'
#cmd2 = 'echo This is python subprocess.'
#final = Popen("{}; {}".format(cmd1, cmd2), shell=True, stdin=PIPE, 
          #stdout=PIPE, stderr=STDOUT, close_fds=True)
#stdout, nothing = final.communicate()
#log = open('log', 'w')
#log.write(stdout)
#log.close()

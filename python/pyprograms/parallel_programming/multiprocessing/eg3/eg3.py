#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 29, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
# Ref: http://stackoverflow.com/questions/15840550/running-script-multiple-times-simultaniously-in-python-2-7


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 29, 2016
#

# Imports
import multiprocessing,os,subprocess
import datetime
import execution  # file: execution.py

#assume we have a function:
#exection.run_main_with_args(filename,name,today_str,dbfolder)

today = datetime.datetime.today()
def my_execute(filename):
    if '.txt' in filename:
       name = filename.strip('.txt')
       dbfolder = "db/" + name
       if not os.path.exists(dbfolder): os.makedirs(dbfolder)
       execution.run_main_with_args(filename,name,str(today),dbfolder)
       
       

p = multiprocessing.Pool()
p.map(my_execute,['file1.txt', 'file2.txt'])

# Author    : Bhishan Poudel
# Date      : Mar 14, 2016
# To delete : rm {0..4}.txt

# Imports
import time
start = time.time()

import os, sys, subprocess, math, re, shutil,copy
from multiprocessing import Process


def func1():
    for x in range(0,5):
        filename = str(x)+".txt"
        print(filename)
        myfile = open(filename,"w")
        string = "This is file "+str(x)+".txt"
        myfile.write(string)
        myfile.close()

def func2():
    for x in range(5,10):
        filename = str(x)+".txt"
        print(filename)
        myfile = open(filename,"w")
        string = "This is file "+str(x)+".txt"
        myfile.write(string)
        myfile.close()

def func3():
    for x in range(10,16):
        filename = str(x)+".txt"
        print(filename)
        myfile = open(filename,"w")
        string = "This is file "+str(x)+".txt"
        myfile.write(string)
        myfile.close()

def func4():
    for x in range(16,22):
        filename = str(x)+".txt"
        print(filename)
        myfile = open(filename,"w")
        string = "This is file "+str(x)+".txt"
        myfile.write(string)
        myfile.close()


#func1()
#func2()
#func3()
#func4()

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

# Running parallel
runInParallel(func1,func2,func3,func4)

end = time.time()
print (end - start)


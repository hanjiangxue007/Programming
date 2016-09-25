#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 07, 2016
# Last update :
#
# Info:
# 1.
#
#

# Imports
from threading import Thread
import time

def timer(name, delay, repeat):
    print("Timer: " + name + " Started")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " Completed")

def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main complete")

if __name__ == '__main__':
    Main()

import os
from multiprocessing import Pool
import time

num_proc = 4
num_calls = 8
sleeper = 0.1

def SomeFunc(arg):
    time.sleep(sleeper)
    print ("%s %5d" % (os.getpid(), arg))
    return arg

proc_pool = Pool(num_proc)
list(proc_pool.imap(SomeFunc, range(num_calls)))

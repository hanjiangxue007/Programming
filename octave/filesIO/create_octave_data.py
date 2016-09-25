import csv
import numpy as np

data=[]
with open('stack25148040.txt','rb') as f:
    r = csv.reader(f, delimiter=' ')
    # csv handles quoted strings with white space
    for l in r:
        # remove empty strings from the split on ' '
        data.append([x for x in l if x])
print data[0]
for dd in data:
    # convert 8 of the strings (per line) to float
    dd[:]=[float(d) for d in dd[:8]]+dd[-1:]

data=data[:-1]  # remove empty last line
print data[0]
print
# make a structured array, with numbers and a string
dt=np.dtype("f8,i4,f8,f8,f8,f8,i4,i4,|S25")
A=np.array([tuple(d) for d in data],dtype=dt)
print A
from scipy.io import savemat
savemat('stack25148040.mat',{'A':A})

# clear; python pyfits2.py 3 psf.txt

import pyfits,sys,os
import numpy as np


os.remove("new1.fits")

z=sys.argv[1] # z is for the argument which we pass for reading col

psf = open('psf.txt')

x=0 # variable to be used as list index	in the for loop

psfile=[]  #this list is for image names
		
datfile=[] # list for weight column

print 'First part: reading from text file'
print '---------------------------------'       
for line in psf:
    part = line.split()
    l=part[0]    # variable l is for copying the image name from col0
    m = part[int(z)]  #variable m for copying weight from column 
    psfile.insert(x,l)
    datfile.insert(x,m)
    print x,psfile[x],datfile[x]
    x=x+1
print '-----------------------------------'
num=0
for p in datfile:
    num = num+float(p)
    print p,num
print 'final sum',num
#print psfile[4],datfile[2]

print 'second part:works on individual image files'

z=np.zeros((601,601))
for l in xrange(0,x):
 print psfile[l]
 f = pyfits.open(psfile[l],mode='update')
 scidata = f[0].data
 print 'original image data', scidata[314,296] # took one array element
 print 'empty data now',z[314,296]
 k=datfile[l]
 print float(k)
 scidata = float(k)*scidata
 z=z+scidata
 print scidata.shape
 print 'data after multiplying ', scidata[314,296] #check what happens when we multiply
 print 'empty data chaged:',z[314,296]
 f.flush()
 f.close() 

z=z/num
hdu=pyfits.PrimaryHDU(z)
hdu.writeto('new1.fits')

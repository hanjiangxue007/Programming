# python plot1.py rq.txt fin.txt


import numpy as np
import matplotlib.pyplot as plt



#f1=sys.argv[1]
#f2=sys.argv[2]

f1='rq.txt'
f2='fin.txt'


# read first file
c1=[]
c2=[]
file1=open(f1,'r')
for l1 in file1:
    p1=l1.split()
    x1=p1[0]
    y1=p1[1]
    c1.append(x1)
    c2.append(y1)
file1.close()

c1=map(float,c1)
c2=map(float,c2)

c2max=max(c2)
#### dividing by maximum value in sed value
#for j in range(len(c2)):
   # c2[j]= c2[j]/c2max

##=============================================================================
###### working on psf file:  psfname wav flux
c3=[]
c4=[]
file2=open(f2,'r')
for l2 in file2:
    p2=l2.split()
    x2=p2[1]
    y2=p2[2]
    c3.append(x2)
    c4.append(y2)
file2.close()

c3=map(float,c3)
c4=map(float,c4)

print c4[0]
c4[0]=c4[0]/0.01075 # rescale flux
c4[0]=c4[0]/c3[0]
c4[0]=c4[0]/c2max
print c4[0]

c4[20]=c4[20]/0.01075
c4[20]=c4[20]/c3[20]
c4[20]=c4[20]/c2max
#####dividing by the  maximum flux value 
c4max=max(c4)




for i in range(1,len(c4)-1):
    c4[i]= c4[i]/0.0215
    c4[i] = c4[i]/c2max
    c4[i] = c4[i]/c3[i]
print c4[0]

#### dividing by maximum value in sed value
for j in range(len(c2)):
    c2[j]= c2[j]/c2max
   # c2[j] = c2[j]/0.0215

   

print c2max,c4max
print('{} {} {} {}'.format('\n\n', ' ', ' ',' ' ))
xa1=np.array(c1)
ya1=np.array(c2)
xa=np.array(c3)
ya=np.array(c4)
plt.plot(xa1,ya1)
plt.plot(xa,ya,'ro')
#plt.savefig('newor.png')
#plt.show()

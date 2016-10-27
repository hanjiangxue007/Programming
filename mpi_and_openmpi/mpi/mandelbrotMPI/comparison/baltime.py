import matplotlib
matplotlib.use('Agg')
import subprocess as sp
import matplotlib.pyplot as plt
from scipy import *


if __name__=="__main__":
    npar=range(2,16,2)
    stim=zeros(len(npar))
    dtim=zeros(len(npar))
    for j,dim in enumerate(npar):
        (stdout,stderr)=sp.Popen("time mpirun -mca btl tcp,self -np %i mandelbrot_dynamic.out" %(dim),shell=True,stdout=sp.PIPE,stderr=sp.PIPE).communicate()
        s1=stderr.split()[1]
        dtim[j]=60*float(s1[:s1.find('m')])+float(s1[s1.find('m')+1:-1])

        (stdout,stderr)=sp.Popen("time mpirun -mca btl tcp,self -np %i mandelbrot_static.out" %(dim),shell=True,stdout=sp.PIPE,stderr=sp.PIPE).communicate()
        s1=stderr.split()[1]
        stim[j]=60*float(s1[:s1.find('m')])+float(s1[s1.find('m')+1:-1])

    fig,ax=plt.subplots(1)
    ax.plot(npar,stim,label="Static")
    ax.plot(npar,dtim,label="Dynamic")
    ax.set_ylabel("Time to run (s)")
    ax.set_xlabel("Number of nodes")
    ax.set_title("Dynamic vs Static Load Balancing")
    ax.legend(loc='best')
    #plt.savefig('loadbalv0.png')
    plt.savefig('loadbalv1.png')

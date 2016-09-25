#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : Jun 30, 2016
 

# Imports
import glob
import matplotlib.pyplot as plt
import numpy as np

filenames = glob.glob('*.sed')
#print(filenames)

colors = ['r', 'b', 'g']





for i in range(len(filenames)):
    infile = filenames[i]
    print('{} {} {}'.format('\ni = ',i, ''))
    print('{} {} {} {}'.format('reading file : ', infile, ' ',' ' ))
    x,y = np.genfromtxt(infile,delimiter=None,usecols=(0,1),dtype=float,unpack=True)


    #==============================================
    ## plot 
    plt.plot(x,y,linewidth=1,color=colors[i],label=infile)

    # title and axes labels
    plt.xlabel('Wavelength (nm) ', fontsize=14)
    plt.ylabel('Flux', fontsize=14)
    plt.legend( loc='upper right', numpoints = 1 )


    # axes limit
    #plt.xlim(300,800)
    #plt.ylim(0,1.2)

    # grid
    plt.grid(True)

    ## save figure
    imagename = 'single.png'
    print('{} {}'.format('output image : ',imagename ))
    plt.savefig(imagename)

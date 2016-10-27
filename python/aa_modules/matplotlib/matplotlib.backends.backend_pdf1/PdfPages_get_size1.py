#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-12-2016 Wed
# Last update :
#
#
# Imports
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

with PdfPages('portrait.pdf') as pdf:
    x = range(10)
    y = [y * 2 for y in x]

    plt.figure()
    plt.clf()
    plt.plot(x, y)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    figure = plt.gcf()
    figure.set_size_inches([7,10])
    pdf.savefig(figure)
    print('Creating portrait.pdf')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : 2016-07-07
 

# Imports
import re

filename = 'broadband.icat'

with open(filename,'r') as fin:
	for line in fin.readlines():
		if line.startswith('object'):
			
			# object line
			object_line = line.strip()
			print(object_line)
			
			# sed line
			sed_line_list = re.findall(r'\S+', object_line)
			sed_line = sed_line_list[5]
			print(sed_line)
			
			# sed name
			sed = sed_line.split("/")[-1]
			print(sed)
			
			# one liner
			mysed = re.findall(r'\S+', line.strip())[5].split("/")[-1]
			print('{} {} {}'.format(r'mysed = ',mysed, ''))
			
			# another one liner
			sed_oneline =  line.split()[-10].split("/")[-1]
			print('{} {} {}'.format(r'sed one liner = ',sed_oneline, ''))

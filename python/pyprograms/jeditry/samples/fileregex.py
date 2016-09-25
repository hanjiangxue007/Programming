#! /usr/bin/env python

# topic: file read in

import re,sys
print

config_file = open(sys.argv[1],'r')
config = {}     # dictionay to store elements of file to be opened

string_regex = re.compile('"(.*?)"')
value_regex = re.compile('[^|\t]*') # if tab is not included everything in line will be printed
                                    # no ^ = values will not be seen
for line in config_file:
    if not line.startswith("#"):
        temp = line.split("=")
        if temp[1].startswith("\""):    # start with "
            config[temp[0]] = string_regex.findall(temp[1]) [0]
        else:
            config[temp[0]] = value_regex.findall(temp[1]) [0]  # is no [0] will print # comments in the config and so on

print config    # this will print the dictionary config
#note that there should be no blank lines in config file

#output: {'salary': '5000 ', 'bonus': '200', 'year ': 'five', 'office': 'athens/ohio'}

#config file:

# #---------------------physics settings-----------------------
# salary=5000 		#starting salary
# office="athens/ohio"	#working office
# year ="five"
# #bonuses
# bonus=200		#per meeting

#this whole thing is a dictionary

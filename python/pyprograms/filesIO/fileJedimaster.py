#! /usr/bin/env python

# topic: reading a file whose name is given in argument
# pre  : there should be a file
# cmd  : clear; python fileJedimaster.py config.txt



import os, sys, subprocess, math, re, shutil,copy

#parse command line inputs
if(len(sys.argv) != 2):
    print("Usage: jedimaster config")
    sys.exit(1);


print "Config file: %s"%sys.argv[1]

#parse config file
config_file = open(sys.argv[1], 'r')
config = {}
string_regex = re.compile('"(.*?)"')
value_regex = re.compile('[^ |\t]*')
for line in config_file:
    if not line.startswith("#"):
        temp = line.split("=")
        if temp[1].startswith("\""):
            config[temp[0]] = string_regex.findall(temp[1])[0]
        else:
            config[temp[0]] = value_regex.findall(temp[1])[0]
print config[0]

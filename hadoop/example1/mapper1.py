#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 24, 2016
# Last update :
# Ref: http://www.glennklockwood.com/data-intensive/hadoop/streaming.html
#
# Run: cat wordcount_in.txt | python mapper1.py

# Imports
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    for key in keys:
        value = 1
        print( "%s\t%d" % (key, value) )

#! /usr/bin/env python

import sys

if (len(sys.argv)!= 3):
    print "\nthe arguments of this program is not three, program is quitting\n"
    sys.exit(1)

print "0th argument: ", sys.argv[0]
print "1st argument: ", sys.argv[1]

# this program should be run in termial.
# python sysarg.py bhishan poudel
# sys.argv[0] = sysarg.py
# sys.argv[1] = bhishan
# sys.argv[2] = poudel




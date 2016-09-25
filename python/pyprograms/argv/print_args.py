#!/usr/bin/env python

from __future__ import print_function
import sys
print(sys.argv, len(sys.argv))

#run this program from terminal
#sample outputs:
# > python print_args.py
# ['print_args.py'] 1
#
# > python print_args.py foo and bar
# ['print_args.py', 'foo', 'and', 'bar'] 4
#
# > python print_args.py "foo and bar"
# ['print_args.py', 'foo and bar'] 2
#
# > python print_args.py "foo and bar" and baz
# ['print_args.py', 'foo and bar', 'and', 'baz'] 4


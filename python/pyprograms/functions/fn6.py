#!/usr/bin/env python
## topic: function returning multiple thing
#  cmd  : clear; python fn6.py

def shut_down(s):
    """The function 'shut_down' returns different answers"""
    
    if s == "yes":
        return "Shutting Down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

# invoking the function
print shut_down("yes")
print shut_down("no")
print shut_down("later")

answer = raw_input("\nType your answer:  ") # raw_input for string input
print shut_down(answer)

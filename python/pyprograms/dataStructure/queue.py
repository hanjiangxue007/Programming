#!/usr/bin/env python

#topic: list as queue
# https://docs.python.org/2/tutorial/datastructures.html

# Using Lists as Queues

from collections import deque
print

queue = deque(["Eric", "John", "Michael"])
print queue                     # deque(['Eric', 'John', 'Michael'])
queue.append("Terry")
print queue                     # deque(['Eric', 'John', 'Michael', 'Terry'])
queue.append("Graham")
print queue                     # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print queue                     # deque(['John', 'Michael', 'Terry', 'Graham'])
queue.popleft()
print queue                     # deque(['Michael', 'Terry', 'Graham'])


# 5.1.2. Using Lists as Queues
#
# It is also possible to use a list as a queue, where the first element added
# is the first element retrieved (?first-in, first-out?); however, lists are not
# efficient for this purpose. While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow
# (because all of the other elements have to be shifted by one).
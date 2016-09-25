#! /usr/bin/env python
#topic: list methods
#source: https://docs.python.org/2/tutorial/datastructures.html

a = [66.25, 333, 333, 1, 1234.5]
print a
print a.count(333), a.count(66.25), a.count('x'), a.count(22) # 2 1 0 0

a.insert(2, -1)     # thrid position is -1
print a             # [66.25, 333, -1, 333, 1, 1234.5]

a.append(333)
print a             #  [66.25, 333, -1, 333, 1, 1234.5, 333]

print a.index(333)  # 1
print a.index(66.25)

a.remove(333)       # removes first 333 in the list
print a             # [66.25, -1, 333, 1, 1234.5, 333]

a.reverse()
print a             # [333, 1234.5, 1, 333, -1, 66.25]

a.sort()
print a             # [-1, 1, 66.25, 333, 333, 1234.5]

a.pop()
print a             # [-1, 1, 66.25, 333, 333]
a.pop(2)            # removes index 2 element in the list
print a

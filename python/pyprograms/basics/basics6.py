#!/usr/bin/env python

# cmd : clear; python basics6.py


#some examples of list
fiboSeq = []
a, b = 0, 1
while (b < 3):
    fiboSeq.append(a)
    a, b = b, a + b  # we cannot indent this line
    print fiboSeq  # [0] [0, 1] [0, 1, 1]
print "answer depend on indentation of print"
print fiboSeq      #[ 0, 1, 1]

print  "**********************************************"
factorial = 1
for i in range(1, 4):
    factorial *= i
print factorial     # 6

print  "**********************************************"
primes = []
for i in range(2, 10):
    for x in range(2, i):
        if (i % x == 0):  # 3%2 == 1 3%3 == 0
            break
    else:
        primes.append(i)
       #print primes
print primes            # [2, 3, 5, 7]

print  "**********************************************"

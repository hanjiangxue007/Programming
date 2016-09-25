#!/usr/bin/env python

# cmd : clear; python basics5.py

print "***************************************"

x = 15

if (x > 6 and x < 10):
    print ("Congrats")

elif (x == 15):
    print ("This is 15")    # This is 15

elif not (4):
    print ("not 6")

else:
    print ("So sad!")

print  "**********************************************"
x = 0
while (x < 10):
    x += 1

    if (x == 5): break

print x     # 5

print  "**********************************************"
x, y = 0, 0
while (True):
    x += 1
    y += 2
    if (x + y > 10):
        break
    print x, y      # 1 2     2 4     3 6
print "if we indent we get different answer"
print x,y           # 4 8

print  "**********************************************"
x = [1, 2, 7] # list
for i in x:
    print i         # 1 2 7
                    # if we do not indent it will not work
print  "**********************************************"
for i in range(2):
    print i         # 0 1

print  "**********************************************"
for i in range(10, 16, 2):
    print i                 # 10 12 14

print  "**********************************************"
print "not divisible by 3"
for i in range(5):
    if not (i % 3):
        continue
    print i     # 1 2 4
                # print i is just below if not
print  "**********************************************"

#!/usr/bin python
# -*- coding: utf-8 -*-


# example 1
people = 30
cars = 40
trucks = 15

if cars > people:
    print ("We should take the cars.\n")
elif cars < people:
    print ("We should not take the cars.\n")
else:
    print("We can't decide.\n")



# example 2
def function(a):
    if a == '1':
        print('1a')
    elif a == '2':
        print('2a')
    else:
        print('3a')

function("1")
function(1)

# using dictionary method
def function(a):
    d={"1":"1a","2":"2a"}
    if not a in d: print("3a")
    else: print((d[a]))
    
function("1")
function(1)

# example 3
def function(a):
    if a not in (1, 2):
        a = 3
    print((str(a) + "a"))
    
function("1")
function(1)
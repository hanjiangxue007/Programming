#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : https://www.quora.com/Is-it-better-to-use-list-comprehensions-or-map-with-a-lambda-function-when-manipulating-elements-in-a-list
# Ref       : http://caisbalderas.com/blog/iterating-with-python-lambdas/

# Examples

# multiply each element by 5
x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x]
print(y)
y = map(lambda v : v * 5, x)
print(y)

# multiply the odd values by 5
# for loop
print("\n")
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
print(y)

# list comprehension
y = [v * 5 for v in x if v % 2]
print(y)

# map lambda filter
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
print(y)


# example 3
# sum each elements of x to each elements of y
# for loop
print("\n\n")
x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
print(z)

# list comprehension
z = [v + w for v in x for w in y]
print(z)
#print(x+y) # catenates elements of y in x

#"pseudo" lambda
t = map(lambda v : map(lambda w : v + w, y), x)
z = sum(t, [])
print(z)

## summary and comparison
#[v + w for v in x for w in y]                              #list comprehension
#map(lambda for v: in map(lambda for w: v + w, in y), in x) #"pseudo" lambda
#map(lambda v : map(lambda w : v + w, y), x)                #lambda


# string filtering
print("\n\n")
garbled = 'spaceX_station'
message = filter(lambda x : x!="X",garbled)
print(message)
# It loop through garbled and put every element unequal to "X" into message.
# There is a loop and a conditional in there already



# for python 2
#When all you’re doing is calling an already-defined function on each element,
#map(f, lst) is a little faster than the corresponding list comprehension
#[f(x) for x in lst]. To an experienced Python programmer,
#I think it’s clearer, too (though Guido may disagree).

#But when evaluating any other expression, [some_expr for x in lst] is faster
#and clearer than map(lambda x: some_expr, lst), because the map incurs an
#extra function call for each element.


# symantics of lambda
funcs = [lambda: x for x in [1, 2, 3, 4, 5]]
print([f() for f in funcs])
#[5, 5, 5, 5, 5]
# but we want
funcs = map(lambda x: lambda: x, [1, 2, 3, 4, 5])
print([f() for f in funcs])
# [1, 2, 3, 4, 5]


# example 2
print("\n\n")
print(map(lambda x: x**2, [1,2,3,4,5]))
print([x**2 for x in [1,2,3,4,5]])




#! /usr/bin/env python
#topic: list methods viz. filter()  map()   reduce()
# https://docs.python.org/2/tutorial/datastructures.html

# There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce().


# filter (function, sequence)
def f(x): return x % 3 == 0 or x % 5 == 0   # to compute a sequence of numbers divisible by 3 or 5
print filter(f, range(2, 25))

# map (function, sequence)
def cube(x): return x*x*x                   # to compute some cubes
print map(cube, range(1, 11))

# reduce (function, sequence)
def add(x,y): return x+y
print add(5,6), add(10,5)
print reduce(add, range(1, 11))             # compute the sum of the numbers 1 through 10
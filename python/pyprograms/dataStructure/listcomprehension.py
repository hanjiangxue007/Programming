#! /usr/bin/env python
#topic: list comprehensions
#source: https://docs.python.org/2/tutorial/datastructures.html

# List comprehensions provide a concise way to create lists.
# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses

squares1 = [x**2 for x in range(10)]
print squares1

squares2 = map(lambda x: x**2, range(10))
print squares2

mylist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print mylist

# Nested list
print "\ngiven matrix"
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
       ]
print matrix

print "\nmethod 1 transpose"
transposed = [[row[i] for row in matrix] for i in range(4)]
print transposed

# this is equivalent to
print "\nmethod 2 transpose"
transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
print transposed

# this is in turn equivalent to
print "\nmethod 3 transpose"
transposed = []
for i in range(4):
     # the following 3 lines implement the nested listcomp
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     transposed.append(transposed_row)
print transposed

# built-in function zip()
print "\nmethod 4"
print zip(*matrix)
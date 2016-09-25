#!/usr/bin/env python

#topic: list
#source: http://www.tutorialspoint.com/python/python_lists.htm
# source: https://docs.python.org/2/tutorial/datastructures.html

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print list1
print list2
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# Updating Lists
list1[3] = 2001
print list1




# The list data type has some more methods. Here are all of the methods of list objects:
#
# list.append(x)
#
#     Add an item to the end of the list; equivalent to a[len(a):] = [x].
#
# list.extend(L)
#
#     Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
#
# list.insert(i, x)
#
#     Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#
# list.remove(x)
#
#     Remove the first item from the list whose value is x. It is an error if there is no such item.
#
# list.pop([i])
#
#     Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# list.index(x)
#
#     Return the index in the list of the first item whose value is x. It is an error if there is no such item.
#
# list.count(x)
#
#     Return the number of times x appears in the list.
#
# list.sort(cmp=None, key=None, reverse=False)
#
#     Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# list.reverse()
#
#     Reverse the elements of the list, in place.
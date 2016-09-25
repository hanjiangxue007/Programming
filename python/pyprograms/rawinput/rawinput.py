#!/usr/bin/python
# cmd : clear; python rawinput.py


# using input
# input determines data type itself
# we must enter "" to type strings

name = input("Type your name within the quotes '' :    ") # eg. 'a'
print("Nice to meet you " + name + "!")

print
age = input("Enter your age:  ") # eg. 3
print("So, you are are already " + str(age) + " y34ears old, " + name + "!")

# raw_input stores all data as string

print
age = raw_input("Enter your age again: ")
print "data type is: ", (age, type(age))


# type casting string into integer

print
age = int(raw_input("Enter your age: "))
print "now data type is: " , (age, type(age))
print




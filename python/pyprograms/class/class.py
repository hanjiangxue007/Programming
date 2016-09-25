#!/usr/bin/python

#   class objects

#   classes, functions etc are called objects
#   lists and dictionaries are mutable objects
#   namespace = objectname.attribute
#   if we copy and paste words from internet it may not be ASCII and not work
#   to overcome this, select the code, right click > File Encoding > US ASCII
#   simple convention: capitalize method name and underscore data attrib

class myClass:
    """A simple example class""" #docstring
    i = 12345          # myClass.i is a data attribute
    def Method(self):  # metod is a function that belongs to an object
                       # myClass.f is method
        return 'hello world'
print myClass.i        # myClass.i is a valid attribute reference
myClass.Method        # myClass.f is a valid attribute reference
                      # myClass.f is a function object
                      # this is a unbound method

#Note: If we type print myClass.f() we get
# TypeError: unbound method f()
#  must be called with myClass instance as first argument

x = myClass()  # this creates a new instance of the class object
               # and assigns this object to the local variable x.
               #this is called instantiation

print x.i
print "\n"
print x.Method()    #this is a bound method
            #x.f is a method object not function object like myClass.f

xf = x.Method  #storing method object in an instance variable
print xf()     # x.Method() doesnot work
print "\n"     # output: hello world

#example 2
class Complex:
     def __init__(self, realpart, imagpart):
         """
            example when method _init_ have 2 arguments
         """
         self.r = realpart
         self.i = imagpart

x = Complex(3.0, -4.5)
print x.r, x.i
print "\n"
#example of Class and Instance variables
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print d.kind                  # shared by all dogs

print e.kind                  # shared by all dogs

print d.name                  # unique to d

print e.name                  # unique to e
print "\n"

#example 2 of Class and Instance variables

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
d.add_trick('runs fast')
e.add_trick('play dead')
e.add_trick('runs slow')

print d.tricks #output: ['roll over', 'runs fast']
print e.tricks #output: ['play dead', 'runs slow']

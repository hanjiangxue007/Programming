#! /usr/bin/env python
#topic: Unpacking Argument Lists
#source: https://docs.python.org/2/tutorial/controlflow.html#tut-unpacking-arguments

print range(3, 6)             # normal call with separate arguments   [3, 4, 5]
args = [3,7]
print range(*args)            # call with arguments unpacked from a list

# n the same fashion, dictionaries can deliver keyword arguments with the **-operator
print "\nexample 2"

def parrot(task=' apply 220 volts to it,', state='dead', action='voom'):
     print "This parrot wouldn't", action,
     print "if you ", task,
     print "it will be", state, "!"
print parrot()

d = {"action": "fly","task": "put it inside a cage,", "state": "trapped"}
print parrot(**d)

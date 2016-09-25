#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 16, 2016
# Last update : 
#
# Inputs      : none
#
# Outputs     : 
#
# Info:
# 1. 
#
#

class Duck:
    def quack(self):
        print("Quack, quack!");

    def fly(self):
        print("Flap, Flap!");

class Person:
    def quack(self):
        print("I'm Quackin'!");

    def fly(self):
        print("I'm Flyin'!");

def in_the_forest(mallard):
    mallard.quack()
    mallard.fly()

in_the_forest(Duck())
in_the_forest(Person())

# In python, better way is use exception handling
print('{} {} {}'.format('\nusing exception handling:','', ''))
mallard = Duck()
try:
    mallard.quack()
except (AttributeError, TypeError):
    print("mallard can't quack()")


##======================================================================
print('{} {} {}'.format('\nexample 3 \n','', ''))
class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()

##======================================================================
print('{} {} {}'.format('\nexample 4\n','', ''))


class Duck(object):
   def quack(self):
      print ("Quack")
 
class Mallard(object):
    def quack(self):
        print ("Quack Quack")
 
def shoot(bird):
    bird.quack()
 
for target in [Duck(), Mallard()]:
   shoot(target)

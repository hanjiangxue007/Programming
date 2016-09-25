#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 07, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1. A class is in the same category of things as variables, 
#      lists, dictionaries, etc. That is, they are objects
# 2. A class is known as a 'data structure' - it holds data, and
#      the methods to process that data.
# 3. A variable inside a class is known as an Attribute.
# 4. A function inside a class is known as a method.
#
#

# define a class
class Pet(object):
    """Pet is a class example."""

    # initialize method
    def __init__(self, name, species):
        self.name = name
        self.species = species
     
    # some methods
    def getName(self):
        return self.name
        
    # some methods
    def getSpecies(self):
        return self.species
 
    # overriding method 
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

# instanciation
polly = Pet("Polly", "Parrot")

# usage (calling from instance)
print(polly.getName())


# calling from class
name = Pet.getName(polly)
print(name)

# usages
print ("Polly is a %s" % polly.getSpecies())
print ("Polly is a %s" % Pet.getSpecies(polly))

# another instance
ginger = Pet("Ginger", "Cat")
ginger.getName()
ginger.getSpecies()

# using overriding method __str__
print(ginger)
print(polly)

##===================================================================
## define a subclass (inheritance from Pet)
class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


#usage
mister_pet = Pet("Mister", "Dog")
mister_dog = Dog("Mister", True)

print(isinstance(mister_pet, Pet))
print(isinstance(mister_pet, Dog))
print(isinstance(mister_dog, Pet))
print(isinstance(mister_dog, Dog))

# call attributes
print('\nprinting attributes')
print(mister_dog.chasesCats())
print(mister_pet.getName())
print(mister_dog.getName())


# some cats and dogs
fido    = Dog("Fido", True)     # name, chases_cats
rover   = Dog("Rover", False)   # name, chases_cats
mittens = Cat("Mittens", True)  # name, hates_dogs
fluffy  = Cat("Fluffy", False)  # name, hates_dogs

print (fido)    # Fido is a Dog
print (rover)   # Rover is a Dog
print (mittens) # Mittens is a Cat
print (fluffy)  # Fuffy is a Cat

print ("%s chases cats: %s" % (fido.getName(), fido.chasesCats()))
# Fido chases cats: True

print ("%s chases cats: %s" % (rover.getName(), rover.chasesCats()))
#Rover chases cats: False

print ("%s hates dogs: %s" % (mittens.getName(), mittens.hatesDogs()))
#Mittens hates dogs: True

print ("%s hates dogs: %s" % (fluffy.getName(), fluffy.hatesDogs()))
#Fluffy hates dogs: False







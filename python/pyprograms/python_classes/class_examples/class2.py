#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 07, 2016
# Last update : 

# Inputs      : none
# Outputs     : 

# Info:
# 1.
#
#

#An example of a class
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
        
# using a class
rectangle = Shape(100,45)

#finding the area of your rectangle:
print (rectangle.area())

#finding the perimeter of your rectangle:
print (rectangle.perimeter())

#describing the rectangle
rectangle.describe("A wide rectangle, more than twice\
 as wide as it is tall")

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)

#re-printing the new area of the rectangle
print (rectangle.area())

# other instances
longrectangle = Shape(120,10)
fatrectangle = Shape(130,120)

# Inheritance
class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x
        
# The shape looks like this:
# _________
#|    |    |
#|    |    |
#|____|____|

class DoubleSquare(Square):
    def __init__(self,y):
        self.x = 2 * y
        self.y = y
    def perimeter(self):
        return 2 * self.x + 3 * self.y        
        

# Pointers and Dictionaries of Classes
print("Pointers and Dictionaries of Classes\n")
# Again, assume the definitions on Shape,
# Square and DoubleSquare have been run.
# First, create a dictionary:
dictionary = {}

# Then, create some instances of classes in the dictionary:
dictionary["DoubleSquare 1"] = DoubleSquare(5)
dictionary["long rectangle"] = Shape(600,45)

#You can now use them like a normal class:
print (dictionary["long rectangle"].area())

dictionary["DoubleSquare 1"].authorName("The Gingerbread Man")
print (dictionary["DoubleSquare 1"].author)



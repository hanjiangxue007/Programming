#!/usr/bin/env python
#author: bhishan poudel
#cmd   : clear; python fn3.py


def clinic():
    """The function clinic is about Going left or right room with repeated option."""

    print
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"

    answer = raw_input("\nType left or right and hit 'Enter' key  ").lower() #raw_input is for keyboard input

    if answer == "left" or answer == "l":
        print "\nThis is wrong room, you cannot go to left!"
    elif answer == "right" or answer == "r":
        print "\nOf course this is the right room, I've told you that already!"
    else:
        print "\nYou didn't pick left or right! Try again."
        clinic()        # this will repeat the whole function again when answer is not left or right

#invoking the function
print clinic.__doc__        # optional: printing the docstring of this fucntion
clinic()
print

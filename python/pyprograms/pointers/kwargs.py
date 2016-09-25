#!/usr/bin/python

#cmd  : clear; python kwargs.py

#kwarg means keyword argument

def func(*args, **kwargs):
    print args, kwargs
func(1, "Welcome", name="thefourtheye", year=2013)

# result: (1, 'Welcome') {'name': 'thefourtheye', 'year': 2013}

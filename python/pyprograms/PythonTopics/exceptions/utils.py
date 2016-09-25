#!/usr/bin/python3

def file2dict(filename):

    dictionary = {}

    data = open(filename, 'r')

    for line in data:
        [ key, value ] = line.split()
        dictionary[key] = value

    data.close()

    return dictionary

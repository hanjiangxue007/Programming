#!/usr/bin/python3

# For the purposes of this topic, the contents of this file
#   should be in a file called utils.py

def file2dict(filename):
    import sys

    dictionary = {}
    data = None

    try:
        data = open(filename, 'r')
        for line in data:
            [ key, value ] = line.split()
            dictionary[key] = value
        data.close()

    except IOError:
        print('Problem with file', filename)
        print('Aborting')
        if type(data) != type(None):
            data.close()
        sys.exit(1)

    return dictionary

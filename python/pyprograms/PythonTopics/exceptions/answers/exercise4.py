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

            try:
                [ key, value ] = line.split()
            except ValueError:
                print('File', filename, 'is not in the correct format.')
                dictionary = None
                break

            dictionary[key] = value

        data.close()

    except IOError as error:
        print('Problem with file', filename+':', error.strerror)
        print('Aborting')
        if type(data) != type(None):
            data.close()
        sys.exit(1)

    return dictionary

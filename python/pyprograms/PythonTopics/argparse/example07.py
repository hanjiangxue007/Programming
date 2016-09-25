import argparse

# Build a basic parser.
help_text = 'Copy a file, line by line, from source to target.'
sign_off = 'Author: Bob Dowling <rjd4@cam.ac.uk>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# Add the command line options

parser.add_argument(                 
    dest='source',  
    type=str,
    metavar='src', 
    help='Source file name'
    )

parser.add_argument(                 
    dest='target',  
    type=str,
    metavar='tgt', 
    help='Target file name'
    )

# Parse the command line
arguments = parser.parse_args()
# print(arguments)

source = open(arguments.source, 'r')
target = open(arguments.target, 'w')

for line in source:
    target.write(line)

target.close()
source.close()


import argparse

# Build a basic parser.
help_text = 'Plot a graph of x=sin(at), y=sin(bt+c), with a graph title.'
sign_off = 'Author: Bob Dowling <rjd4@cam.ac.uk>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# Parse the command line
arguments = parser.parse_args()
print(arguments)


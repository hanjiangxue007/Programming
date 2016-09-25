import argparse

# Build a basic parser.
help_text = 'Be very verbose'
sign_off = 'Author: Bob Dowling <rjd4@cam.ac.uk>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# Add the command line options
parser.add_argument(
    '-v',
    '--verbose',
    dest='verbosity',
    action='count',
    default=0,
    help='Repeat this flag to be even more verbose'
    )

# Parse the command line
arguments = parser.parse_args()
print(arguments)


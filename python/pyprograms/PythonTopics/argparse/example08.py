import argparse


help_text = 'A simple tool to count the characters, words and lines in a series of files. '
sign_off = '(c) Bob Dowling, 2012'
parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

parser.add_argument(
    dest='filenames',
    type=str,
    action='store',
    nargs='*',
    help='Names of files to be analyzed.'
    )

arguments = parser.parse_args()
print(arguments)


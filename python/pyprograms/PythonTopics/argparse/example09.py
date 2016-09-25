import argparse

def statistics(filename):
    n_chars = 0
    n_words = 0
    n_lines = 0
    data = open(filename, 'r')
    for line in data:
        n_lines += 1
        n_chars += len(line)
        n_words += len(line.split())
    data.close()
    return(n_lines, n_words, n_chars)


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


for filename in arguments.filenames:
    print(filename, statistics(filename))


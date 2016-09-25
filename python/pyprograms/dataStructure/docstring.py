#! /usr/bin/env python
#topic:docstring
#source: https://docs.python.org/2/tutorial/controlflow.html#tut-unpacking-arguments

# There are emerging conventions about the content and formatting of documentation strings.
# The first line should always be a short, concise summary of the objects purpose
# This line should begin with a capital letter and end with a period.

# second line = blanck
# next lines = describe the objects calling conventions, its side effects, etc.

def my_function():
     """Do nothing, but document it.        # first line is small
                                            # second line is empty
     No, really, it doesn't do anything.
     """
     pass

print my_function.__doc__

# # description:
# The Python parser does not strip indentation from multi-line string literals in Python,
# so tools that process documentation have to strip indentation if desired.
# This is done using the following convention.
# The first non-blank line after the first line of the string determines
# the amount of indentation for the entire documentation string.
# (We can?t use the first line since it is generally adjacent to the string?s opening
# quotes so its indentation is not apparent in the string literal.)
# Whitespace ?equivalent? to this indentation is then stripped from the
# start of all lines of the string. Lines that are indented less should not occur,
# but if they occur all their leading whitespace should be stripped.
# Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).
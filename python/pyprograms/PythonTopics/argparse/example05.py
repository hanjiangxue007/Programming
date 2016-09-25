import argparse

# Build a basic parser.
help_text = 'Plot a graph of x=sin(at), y=sin(bt+c), with graph title provided by the user.'
sign_off = 'Author: Bob Dowling <rjd4@cam.ac.uk>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# Add the command line options
parser.add_argument(
    '-n', 
    '--npts',  
    dest='npts',  
    type=int,   
    default=512, 
    metavar='n', 
    help='Number of points to plot'
    )

parser.add_argument(
    '-x', 
    '--xfreq', 
    dest='xfreq', 
    type=float, 
    default=1.0, 
    metavar='a', 
    help='Frequency of the x-oscillation'
    )

parser.add_argument(
    '-y', 
    '--yfreq', 
    dest='yfreq', 
    type=float, 
    default=1.0, 
    metavar='b', 
    help='Frequency of the y-oscillation'
    )

parser.add_argument(
    '-p', 
    '--phase', 
    dest='phase', 
    type=float, 
    default=0.0, 
    metavar='c', 
    help='Phase difference between the x- and y-oscillations measured in radians'
    )

parser.add_argument(
    '-t', 
    '--title', 
    dest='title', 
    type=str, 
    default='',  
    metavar='title', 
    help='Title of graph'
    )

parser.add_argument(                 
    dest='filename',  
    type=str,
    metavar='fname', 
    help='File name for graph (required)'
    )

# Parse the command line
arguments = parser.parse_args()
print(arguments)


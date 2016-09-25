import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data05x
y = plotdata.data05y

half = plotdata.data05half
quarter = plotdata.data05quarter

# Plot y against x
pyplot.errorbar(x,y, yerr=(quarter,half))

pyplot.title('Example 05b')
pyplot.savefig('example05b.png')

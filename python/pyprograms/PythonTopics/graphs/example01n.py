import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Set axis labels
pyplot.xlabel('$-1<x<1$')
pyplot.ylabel('$x^{3}$', rotation='horizontal')

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01n.png')

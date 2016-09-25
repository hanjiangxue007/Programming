import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Set a title
pyplot.title('y = x cubed\nfrom x=-1 to x=1', verticalalignment='center')

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01j.png')

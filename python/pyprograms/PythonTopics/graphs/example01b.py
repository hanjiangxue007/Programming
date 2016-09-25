import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Set the x-ticks to be every 0.25
pyplot.xticks([0.25*k for k in range(-4,5)])

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01b.png')

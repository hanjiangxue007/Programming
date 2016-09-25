import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Set the axes
# pyplot.axis((Xmin, Xmax, Ymax, Ymax))
pyplot.axis([-1.5, 1.5, -1.5, 1.5])

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01a.png')

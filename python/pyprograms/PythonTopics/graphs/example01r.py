import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Plot y against x
pyplot.plot(x,y, color='green', linestyle='dashed', linewidth=5)

pyplot.savefig('example01r.png')

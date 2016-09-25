import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

pyplot.xticks([])
pyplot.yticks([])
pyplot.box('off')

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01s.png')

import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Plot y against x
line = pyplot.plot(x,y, label='x cubed')

# Set a legend
pyplot.legend(title='The legend')

pyplot.savefig('example01q.png')

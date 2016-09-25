# import the graphics module being used
import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lists of floating point numbers
x = plotdata.exercise02x
ya = plotdata.exercise02a
yb = plotdata.exercise02b

# Pre-plot
pyplot.title('Exercise 2')

# Plot y against x
pyplot.plot(x, ya, label='$y=x^{1/2}$')
pyplot.plot(x, yb, label='$y=x^{2}$')

# Post-plot
pyplot.legend(loc='lower right', title='Curves drawn:')

# Output the graph
pyplot.savefig('exercise02.png')

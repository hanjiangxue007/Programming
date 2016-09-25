# import the graphics module being used
import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lists of floating point numbers
x = plotdata.exercise01x
y = plotdata.exercise01y

# Pre-plot
pyplot.axis([-1.5, 1.5, -1.5, 1.5])
pyplot.xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
pyplot.yticks([-1.0, -(0.5**(1/3)), 0.0, 0.5**(1/3), 1.0], ['$-1$', '$-{1/2}^{1/3}$', '$0$', '${1/2}^{1/3}$', '$1$'])
pyplot.title('Exercise 1')
pyplot.xlabel('$-1<x<1$')
pyplot.ylabel('$x^{1/3}$')

# Plot y against x
pyplot.plot(x,y, color='red', linewidth=2.5, label='$y=x^{1/3}$')

# Post-plot
pyplot.legend(loc='lower right', title='Curve drawn:')

# Output the graph
pyplot.savefig('exercise01.png')

# import the graphics module being used
import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# The various y are values of the Chebyshev polynomials
x = plotdata.data03yc # T_3(x)
y = plotdata.data03yd # T_4(x)

# Pre-plot
pyplot.title('Exercise 3')

# Plot y against x
pyplot.plot(x,y)

# Output the graph
pyplot.savefig('exercise03.png')

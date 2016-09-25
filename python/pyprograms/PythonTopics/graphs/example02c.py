import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# Plot y against x
pyplot.plot(plotdata.data03x, plotdata.data03ya, label='$T_{1}(x)$')
pyplot.plot(plotdata.data03x, plotdata.data03yb, label='$T_{2}(x)$')
pyplot.plot(plotdata.data03x, plotdata.data03yc, label='$T_{3}(x)$')

# Set a legend
pyplot.legend(loc='lower right')

# Set a title
pyplot.title('Example 02c')

pyplot.savefig('example02c.png')

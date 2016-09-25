import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# Plot y against x
pyplot.plot(plotdata.data02x, plotdata.data02ya, label='$T_{1}(x)$')
pyplot.plot(plotdata.data02x, plotdata.data02yb, label='$T_{2}(x)$')
pyplot.plot(plotdata.data02x, plotdata.data02yc, label='$T_{3}(x)$')

# Set a legend
pyplot.legend(loc='lower right')

# Set a title
pyplot.title('Example 02b')

pyplot.savefig('example02b.png')

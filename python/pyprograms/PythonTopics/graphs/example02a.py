import matplotlib.pyplot as pyplot
import plotdata

# Plot y against x
pyplot.plot(plotdata.data02x, plotdata.data02ya, label='$T_{1}(x)$')

# Set a legend
pyplot.legend(loc='lower right')

# Set a title
pyplot.title('Example 02a')

# Create the graph
pyplot.savefig('example02a.png')

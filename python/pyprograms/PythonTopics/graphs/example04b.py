import matplotlib.pyplot as pyplot

# Get some data to plot
import plotdata
x = plotdata.data04x
y = plotdata.data04yb

# Plot y against x
pyplot.scatter(x, y)

# Set a title
pyplot.title('Example 04b')

pyplot.savefig('example04b.png')

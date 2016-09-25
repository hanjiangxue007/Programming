import matplotlib.pyplot as pyplot

# Get some data to plot
import plotdata
x = plotdata.data04x
y = plotdata.data04yb

# Plot y against x
pyplot.plot(x, y, linestyle='', marker='o')

# Set a title
pyplot.title('Example 04a')

pyplot.savefig('example04a.png')

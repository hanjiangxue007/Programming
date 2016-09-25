import matplotlib.pyplot as pyplot

# Get some data to plot
import plotdata
x = plotdata.data04x
y = plotdata.data04yb

# Plot y against x
pyplot.plot(x, y, linestyle='', marker='o', markersize=15.0, markeredgewidth=5.0, markerfacecolor='green', markeredgecolor='red')

# Set a title
pyplot.title('Example 04c')

pyplot.savefig('example04c.png')

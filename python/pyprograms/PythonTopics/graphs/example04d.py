import matplotlib.pyplot as pyplot

# Get some data to plot
import plotdata
x = plotdata.data04u
y = plotdata.data04v

# Plot y against x
pyplot.plot(x, y, linestyle='', marker=',', markerfacecolor='blue')

# Set a title
pyplot.title('Example 04d')

pyplot.savefig('example04d.png')

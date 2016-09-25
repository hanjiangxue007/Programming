import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data05x
y = plotdata.data05y

# Plot y against x
pyplot.errorbar(x,y)

pyplot.title('Example 05a')
pyplot.savefig('example05a.png')

import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data05x
y = plotdata.data05y

yminus = plotdata.data05ym
yplus  = plotdata.data05yp

# Plot y against x
pyplot.errorbar(x,y, yerr=(yminus,yplus))

pyplot.title('Example 05c')
pyplot.savefig('example05c.png')

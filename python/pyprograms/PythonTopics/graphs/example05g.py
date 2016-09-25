import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data05x
y = plotdata.data05y

yminus = plotdata.data05ym
yplus  = plotdata.data05yp

# Plot y against x
pyplot.errorbar(x,y, yerr=(yminus,yplus), linestyle='dashed', color='red', linewidth=5.0, marker='o', markeredgecolor='red', markeredgewidth=5, markerfacecolor='white', markersize=15, ecolor='black', elinewidth=10.0, capsize=0)

pyplot.title('Example 05g')
pyplot.savefig('example05g.png')

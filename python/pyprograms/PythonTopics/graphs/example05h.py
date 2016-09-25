import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data05x
y = plotdata.data05y

xminus = plotdata.data05xm
xplus  = plotdata.data05xp

yminus = plotdata.data05ym
yplus  = plotdata.data05yp

# Plot y against x
pyplot.errorbar(x,y, xerr=(xminus,xplus), yerr=(yminus,yplus))

pyplot.title('Example 05h')
pyplot.savefig('example05h.png')

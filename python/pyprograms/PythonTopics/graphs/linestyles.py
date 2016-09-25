import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

linestyles = [
    'solid',
    'dashed',
    'dotted'
    ]
# Plot y against x
for index in range(len(linestyles)):
    linestyle = linestyles[index]
    yy = [ yval+index*0.1 for yval in y]
    pyplot.plot(x,yy, linestyle=linestyle, color='blue', label=linestyle)

pyplot.legend(loc='upper left')
pyplot.savefig('linestyles.png')

import matplotlib.pyplot as pyplot
import plotdata

# Using NumPy arrays for the x-values
import numpy
x1 = numpy.array(plotdata.data08x)

x2 = x1 + 0.25
x3 = x1 + 0.50

y1 = plotdata.data08y1
y2 = plotdata.data08y2
y3 = plotdata.data08y3

pyplot.bar(x1,y1, width=0.25, color='blue')
pyplot.bar(x2,y2, width=0.25, color='green')
pyplot.bar(x3,y3, width=0.25, color='red')

pyplot.title('Example 08h')
pyplot.savefig('example08h.png')

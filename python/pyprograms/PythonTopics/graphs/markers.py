import matplotlib.pyplot as pyplot
import numpy
import numpy.random

markers1 = [ 'o', '.', ',', 'v', '<', '>', '^' ]
markers2 = [ 'D', 'd', 'h', 'H', '*' ]
markers3 = [ 'x', '+', '|', '1', '2', '3', '4' ]

# Plot y against x
for marker in markers3:
    x = numpy.random.random(10)
    y = numpy.random.random(10)
    pyplot.plot(x, y, linestyle='', marker=marker, markeredgecolor='blue', markerfacecolor='red', label=marker)

pyplot.legend(loc='lower left')

pyplot.savefig('markers3.png')

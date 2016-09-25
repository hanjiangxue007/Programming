import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Arbitrary y-ticks
pyplot.yticks([-0.9, -0.4, 0.0, 0.3, 0.6, 0.85], ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta'])

# Plot y against x
pyplot.plot(x,y)

pyplot.savefig('example01d.png')

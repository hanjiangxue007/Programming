import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# x and y are lits of floating point numbers
x = plotdata.data01x
y = plotdata.data01y

# Plot y against x
pyplot.plot(x,y, label='$y=x^{3}$')

# Set a legend
locations = [
    'best',
    'upper right',
    'upper left',
    'lower left',
    'lower right',
    'right',
    'center left',
    'center right',
    'lower center',
    'upper center',
    'center'
    ]
for index in range(len(locations)):
    location = locations[index]
    pyplot.legend(loc=location, title=location)
    pyplot.savefig('legends_pre.png', transparent=True)


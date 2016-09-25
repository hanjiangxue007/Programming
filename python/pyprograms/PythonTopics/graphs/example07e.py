import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data, rwidth=0.75)

pyplot.title('Example 07e')
pyplot.savefig('example07e.png')

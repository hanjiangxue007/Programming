import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data, bins=20)

pyplot.title('Example 07h')
pyplot.savefig('example07h.png')

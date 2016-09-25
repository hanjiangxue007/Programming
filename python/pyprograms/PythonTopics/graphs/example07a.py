import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data)

pyplot.title('Example 07a')
pyplot.savefig('example07a.png')

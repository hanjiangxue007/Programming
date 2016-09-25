import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data, color='green')

pyplot.title('Example 07d')
pyplot.savefig('example07d.png')

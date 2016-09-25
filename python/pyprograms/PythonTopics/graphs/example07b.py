import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.axis([-10.0,10.0,0.0,250.0])
pyplot.hist(data)

pyplot.title('Example 07b')
pyplot.savefig('example07b.png')

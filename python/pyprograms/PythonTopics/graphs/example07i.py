import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data, bins=[-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0])

pyplot.title('Example 07i')
pyplot.savefig('example07i.png')

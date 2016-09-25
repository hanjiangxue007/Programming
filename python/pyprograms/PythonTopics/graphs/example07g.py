import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data, orientation='horizontal')

pyplot.title('Example 07g')
pyplot.savefig('example07g.png')

import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist([data[:750], data[750:]])

pyplot.title('Example 07j')
pyplot.savefig('example07j.png')

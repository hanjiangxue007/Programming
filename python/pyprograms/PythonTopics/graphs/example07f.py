import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist(data[:750], rwidth=0.5)
pyplot.hist(data[750:], rwidth=0.5)

pyplot.title('Example 07f')
pyplot.savefig('example07f.png')

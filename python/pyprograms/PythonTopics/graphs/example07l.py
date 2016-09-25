import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist([data[:750], data[750:]], color=['red', 'yellow'])

pyplot.title('Example 07l')
pyplot.savefig('example07l.png')

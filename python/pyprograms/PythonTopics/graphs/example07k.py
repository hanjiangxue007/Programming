import matplotlib.pyplot as pyplot
import plotdata

data = plotdata.data07

pyplot.hist([data[:750], data[750:]], histtype='barstacked')

pyplot.title('Example 07k')
pyplot.savefig('example07k.png')

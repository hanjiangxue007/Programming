import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y = plotdata.data08y

pyplot.bar(x,y)

pyplot.title('Example 08a')
pyplot.savefig('example08a.png')

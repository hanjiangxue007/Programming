import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y = plotdata.data08y

pyplot.bar(x,y, width=0.25)

pyplot.title('Example 08c')
pyplot.savefig('example08c.png')

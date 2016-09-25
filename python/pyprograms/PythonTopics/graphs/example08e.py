import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y = plotdata.data08y

pyplot.bar(x,y, color='green', edgecolor='red', linewidth=5.0)

pyplot.title('Example 08e')
pyplot.savefig('example08e.png')

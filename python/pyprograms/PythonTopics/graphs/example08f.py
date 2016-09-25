import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y1 = plotdata.data08y1
y2 = plotdata.data08y2

pyplot.bar(x,y1,y2)

pyplot.title('Example 08f')
pyplot.savefig('example08f.png')

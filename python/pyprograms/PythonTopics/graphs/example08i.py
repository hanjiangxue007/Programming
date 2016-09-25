import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x

upper = plotdata.data08y1
lower = plotdata.data08y2

pyplot.bar(x, upper, bottom=lower)

pyplot.title('Example 08i')
pyplot.savefig('example08i.png')

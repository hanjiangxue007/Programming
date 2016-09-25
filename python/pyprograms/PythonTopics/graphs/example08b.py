import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y = plotdata.data08y

pyplot.bar(x,y, align='center')

pyplot.title('Example 08b')
pyplot.savefig('example08b.png')

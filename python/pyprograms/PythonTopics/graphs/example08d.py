import matplotlib.pyplot as pyplot
import plotdata

x = plotdata.data08x
y = plotdata.data08y
wlist = plotdata.data08w

pyplot.bar(x,y, width=wlist)

pyplot.title('Example 08d')
pyplot.savefig('example08d.png')

import matplotlib.pyplot as pyplot
import plotdata

# Using Python lists for the x-values
x1 = plotdata.data08x
x2 = [ x + 0.25 for x in x1 ]
x3 = [ x + 0.50 for x in x1 ]

y1 = plotdata.data08y1
y2 = plotdata.data08y2
y3 = plotdata.data08y3

pyplot.bar(x1,y1, width=0.25, color='blue')
pyplot.bar(x2,y2, width=0.25, color='green')
pyplot.bar(x3,y3, width=0.25, color='red')

pyplot.title('Example 08g')
pyplot.savefig('example08g.png')

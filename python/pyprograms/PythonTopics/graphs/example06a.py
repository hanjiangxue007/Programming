import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

pyplot.polar(t,r)

pyplot.title('Example 06a')
pyplot.savefig('example06a.png')


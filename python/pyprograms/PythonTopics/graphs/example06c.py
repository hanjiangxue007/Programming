import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

pyplot.thetagrids([0.0, 90.0, 180.0, 270.0])

pyplot.polar(t,r)

pyplot.title('Example 06c')
pyplot.savefig('example06c.png')


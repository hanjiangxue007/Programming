import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

pyplot.thetagrids([0.0, 90.0, 180.0, 270.0], labels=['E', 'N', 'W', 'S'])

pyplot.polar(t,r)

pyplot.title('Example 06d')
pyplot.savefig('example06d.png')


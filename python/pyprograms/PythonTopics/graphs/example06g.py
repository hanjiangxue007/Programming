import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

# ylim() sets the upper r value.
pyplot.ylim(ymax=8.0)
pyplot.rgrids([2.0, 4.0, 6.0, 8.0])

pyplot.polar(t,r)

pyplot.title('Example 06g')
pyplot.savefig('example06g.png')


import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

# ylim() sets the upper r value.
pyplot.ylim(ymax=8.0)
pyplot.rgrids([1.57, 3.14, 4.71, 6.28], labels=['$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])

pyplot.polar(t,r)

pyplot.title('Example 06i')
pyplot.savefig('example06i.png')


import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

# ylim() sets the upper r value.
pyplot.ylim(ymax=8.0)
pyplot.rgrids([1.57, 3.14, 4.71, 6.28], labels=['π/2', 'π', '3π/2', '2π'], angle=-22.5)

pyplot.polar(t,r)

pyplot.title('Example 06j')
pyplot.savefig('example06j.png')


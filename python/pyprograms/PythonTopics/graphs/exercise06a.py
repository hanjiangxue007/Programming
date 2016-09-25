import matplotlib.pyplot as pyplot
import plotdata


# Base data
# t contains the theta values
# r contains the radial values
t = plotdata.exercise06t
r = plotdata.exercise06r

pyplot.axes(polar=True)

pyplot.thetagrids([0, 90, 180, 270], ['$0$', '$\pi/2$', '$\pi$', '$3\pi/2$'])
pyplot.rgrids([0.5, 1.0], angle=30)

pyplot.polar(t,r)

pyplot.title('Exercise 6')
pyplot.savefig('exercise06.png')


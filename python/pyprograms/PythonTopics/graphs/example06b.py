import matplotlib.pyplot as pyplot
import plotdata

pyplot.axes(polar=True)

t = plotdata.data06t
r = plotdata.data06r

pyplot.polar(t,r, linestyle='dashed', linewidth=2.5, color='red', marker='.', markersize=7.5, markeredgecolor='blue', markeredgewidth=1.5, markerfacecolor='green')

pyplot.title('Example 06b')
pyplot.savefig('example06b.png')


import matplotlib.pyplot as pyplot
import plotdata

pyplot.title('Exercise 8')

# The data:
# plotdata.exercise08x - the base x-values

# Make bars width 0.2 to leave a 0.2 gap between sets.

# plotdata.exercise08y1a - the upper values for the first dataset
# plotdata.exercise08y1b - the lower values for the first dataset
# To be plotted in blue

x1 = plotdata.exercise08x
pyplot.bar(x1, plotdata.exercise08y1a, bottom=plotdata.exercise08y1b, width=0.2, color='blue')

# plotdata.exercise08y2a - the upper values for the second dataset
# plotdata.exercise08y2b - the lower values for the second dataset
# To be plotted in green

x2 = [ x + 0.2 for x in x1 ]
pyplot.bar(x2, plotdata.exercise08y2a, bottom=plotdata.exercise08y2b, width=0.2, color='green')

# plotdata.exercise08y3a - the upper values for the third dataset
# plotdata.exercise08y3b - the lower values for the third dataset
# To be plotted in yellow

x3 = [ x + 0.4 for x in x1 ]
pyplot.bar(x3, plotdata.exercise08y3a, bottom=plotdata.exercise08y3b, width=0.2, color='yellow')

# plotdata.exercise08y4a - the upper values for the fourth dataset
# plotdata.exercise08y4b - the lower values for the fourth dataset
# To be plotted in red

x4 = [ x + 0.6 for x in x1 ]
pyplot.bar(x4, plotdata.exercise08y4a, bottom=plotdata.exercise08y4b, width=0.2, color='red')




pyplot.savefig('exercise08a.png')

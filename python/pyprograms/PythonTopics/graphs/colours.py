import matplotlib.pyplot as pyplot

# plotdata is a local module for our convenience
import plotdata

# Plot y against x
pyplot.plot(plotdata.data02x, plotdata.data02ya, label='1 blue')
pyplot.plot(plotdata.data02x, plotdata.data02yb, label='2 green')
pyplot.plot(plotdata.data02x, plotdata.data02yc, label='3 red')
pyplot.plot(plotdata.data02x, plotdata.data02yd, label='4 cyan')
pyplot.plot(plotdata.data02x, plotdata.data02ye, label='5 magenta')
pyplot.plot(plotdata.data02x, plotdata.data02yf, label='6 bilious yellow')
pyplot.plot(plotdata.data02x, plotdata.data02yg, label='7 grey')

# Set a legend
pyplot.legend(loc='lower right')

pyplot.savefig('colours.png')

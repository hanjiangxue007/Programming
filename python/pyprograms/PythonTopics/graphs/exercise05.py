import matplotlib.pyplot as pyplot
import plotdata

pyplot.title('Exercise 5')

# Base data
x = plotdata.exercise05x
y = plotdata.exercise05y

# These values are for the red thick bars
yminus_inner = plotdata.exercise05y1
yplus_inner  = plotdata.exercise05y2

# These values are for the blue thin  bars
yminus_outer = plotdata.exercise05y3
yplus_outer =  plotdata.exercise05y4

# You need to write *two* calls to pyplot.errorbar
pyplot.errorbar(XXXX)
pyplot.errorbar(XXXX)

pyplot.savefig('exercise05.png')


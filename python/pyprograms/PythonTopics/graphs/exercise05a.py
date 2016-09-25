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

pyplot.errorbar(x,y, yerr=(yminus_outer,yplus_outer), linestyle='', marker='', ecolor='blue', elinewidth=1.0, capsize=5.0)
pyplot.errorbar(x,y, yerr=(yminus_inner,yplus_inner), linestyle='', marker='', ecolor='red',  elinewidth=5.0, capsize=0)

pyplot.savefig('exercise05.png')


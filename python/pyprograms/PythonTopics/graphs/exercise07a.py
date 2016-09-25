import matplotlib.pyplot as pyplot
import plotdata

pyplot.title('Exercise 7')

# Base data
data1 = plotdata.exercise07a
data2 = plotdata.exercise07b
data3 = plotdata.exercise07c

pyplot.hist([data1, data2, data3], histtype='barstacked', color=['green', 'orange', 'red'])

pyplot.savefig('exercise07.png')

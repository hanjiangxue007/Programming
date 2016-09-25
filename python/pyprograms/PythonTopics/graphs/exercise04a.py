import matplotlib.pyplot as pyplot
import numpy

def make_data(epsilon):
    N = 100
    n_iters = 1000
    x = ((numpy.zeros(N) + 1.0).reshape(N,1) * numpy.linspace(0.0, 1.0, N).reshape(1,N)).flatten()
    y = ((numpy.zeros(N) + 1.0).reshape(1,N) * numpy.linspace(0.0, 1.0, N).reshape(N,1)).flatten()
    for count in range(0, n_iters):
        (x, y) = ((x+y)%1.0, (y*(1.0 + epsilon*numpy.sin(2.0*numpy.pi*x)))%1.0)
    return(x,y)

pyplot.title('Exercise 4')

(x,y) = make_data(0.5)
pyplot.plot(x,y,linestyle='', marker=',', markerfacecolor='red',   label='0.500 red')

(x,y) = make_data(0.525)
pyplot.plot(x,y,linestyle='', marker=',', markerfacecolor='green', label='0.525 green')

(x,y) = make_data(0.55)
pyplot.plot(x,y,linestyle='', marker=',', markerfacecolor='blue',  label='0.550 blue')

pyplot.legend(loc='lower right')

pyplot.savefig('exercise04.png')

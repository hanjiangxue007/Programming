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


(x,y) = make_data(0.5)
# Plot (x,y) with red pixels

(x,y) = make_data(0.525)
# Plot (x,y) with green pixels

(x,y) = make_data(0.55)
# Plot (x,y) with blue pixels



pyplot.savefig('exercise04.png')

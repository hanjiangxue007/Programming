# Bhishan Poudel
# Dec 3, 2015 Thu

# clear; python fit3.py; rm *~

from numpy import *
from matplotlib.pyplot import *

x = [2.53240, 1.91110, 1.18430, 0.95784, 0.33158,
     -0.19506, -0.82144, -1.64770, -1.87450, -2.2010]

y = [-2.50400, -1.62600, -1.17600, -0.87400, -0.64900,
     -0.477000, -0.33400, -0.20600, -0.10100, -0.00600]

coefficients = polyfit(x, y, 6)
polynomial = poly1d(coefficients)
xs = arange(-2.2, 2.6, 0.1)
ys = polynomial(xs)

plot(x, y, 'o')
plot(xs, ys)
ylabel('y')
xlabel('x')
show()


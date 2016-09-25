"""This module contains trial data or functions to generate trial data
for the UCS self-paced course on plotting graphs with matplotlib.pyplot.
Having it avoids the need to explain other data processing modules used
to generate the data, helping the student focus on the plotting aspects.

Bob Dowling <rjd4@cam.ac.uk>
2012
"""

import numpy
import numpy.polynomial
import numpy.random

import pickle

def chebs(x, n):
    '''Calculates Chebyshev functions of the first kind using the trigonometric functions.'''

    answers = []
    for m in range(1,n+1):
        series = numpy.zeros(n+1)
        series[m] = 1.0
        answers.append(numpy.polynomial.Chebyshev(series)(x))

    return answers





data01x = numpy.linspace(-1.0, 1.0, 201)
data01y = data01x**3

exercise01x = data01y
exercise01y = data01x

data02x = data01x
data02theta = numpy.arccos(data02x)
[data02ya, data02yb, data02yc, data02yd, data02ye, data02yf, data02yg] = chebs(data02x, 7)

data03x = numpy.linspace(-1.5, 1.5, 201)
[data03ya, data03yb, data03yc, data03yd, data03ye] = chebs(data03x, 5)

exercise02x = numpy.linspace(0.0, 1.0, 101)
exercise02a = exercise02x**0.5
exercise02b = exercise02x**2.0


data04x = numpy.linspace(-1.0, 1.0, 21)
[data04ya, data04yb, data04yc, data04yd, data04ye] = chebs(data04x, 5)

data04u = numpy.random.random(10000) - numpy.random.random(10000)
data04v = data04u**2 + 0.25*numpy.random.random(10000)

# data05theta = numpy.linspace(-2.0*numpy.pi, 2.0*numpy.pi, 61)
# data05radius = data05theta

data05x = numpy.linspace(1.0, 10.0, 11) - 0.5 + numpy.random.random(11)
data05y = 1.0/data05x

data05half = numpy.zeros(len(data05x)) + 0.5
data05quarter = numpy.zeros(len(data05x)) + 0.25

data05xp = 0.5*numpy.random.random(len(data05x))
data05xm = 0.5*numpy.random.random(len(data05x))
data05yp = data05y*(1.0 + 0.5*numpy.random.random(len(data05x)))
data05ym = data05y*(1.0 - 0.5*numpy.random.random(len(data05x)))

exercise05n = 41
exercise05x = numpy.linspace(1.0, 20.0, exercise05n)
exercise05y = numpy.log(exercise05x) + numpy.random.random(exercise05n)*0.1
exercise05y1 = exercise05y*0.2*(1.0 + numpy.random.random(exercise05n))
exercise05y2 = exercise05y*0.2*(1.0 + numpy.random.random(exercise05n))
exercise05y3 = exercise05y1*(1.0 + numpy.random.random(exercise05n))
exercise05y4 = exercise05y2*(1.0 + numpy.random.random(exercise05n))

data06n = 41
data06t = numpy.linspace(0.0, 2.0*numpy.pi, data06n)
data06r = data06t

exercise06n = 121
exercise06t = numpy.linspace(0.0, 2.0*numpy.pi, exercise06n)
exercise06r = numpy.sin(3.0*exercise06t)**2

data07n = 1000
data07  = list(numpy.random.normal(-2.0, 1.0, data07n//2)) + list(numpy.random.normal(2.0, 1.0, data07n//2))

exercise07n = 1000
exercise07a = numpy.random.normal(-1.0, 1.0, exercise07n)
exercise07b = numpy.random.normal( 0.0, 1.0, exercise07n)
exercise07c = numpy.random.normal( 1.0, 1.0, exercise07n)

data08n = 10
data08x = numpy.linspace(1.0, float(data08n), data08n)

data08y = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 + 0.5*numpy.random.random(data08n))
data08w = 0.24 + 0.5*numpy.random.random(data08n)
data08y1 = data08y
data08y2 = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 - 0.5*numpy.random.random(data08n))
data08y3 = 1.0 + numpy.linspace(1.0, float(data08n), data08n)

exercise08n = 20
exercise08x = numpy.linspace(1.0, float(data08n), data08n)

exercise08y1a = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 + 0.5*numpy.random.random(data08n))
exercise08y1b = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 - 0.5*numpy.random.random(data08n))

exercise08y2a = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 + 0.5*numpy.random.random(data08n))
exercise08y2b = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 - 0.5*numpy.random.random(data08n))

exercise08y3a = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 + 0.5*numpy.random.random(data08n))
exercise08y3b = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 - 0.5*numpy.random.random(data08n))

exercise08y4a = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 + 0.5*numpy.random.random(data08n))
exercise08y4b = (1.0 + numpy.linspace(1.0, float(data08n), data08n))*(1.0 - 0.5*numpy.random.random(data08n))

datafile = open('plotdata.pck', 'wb')
data = pickle.Pickler(datafile)


data.dump(list(data01x))
data.dump(list(data01y))

data.dump(list(exercise01x))
data.dump(list(exercise01y))

data.dump(list(data02x))
data.dump(list(data02theta))

data.dump(list(data02ya))
data.dump(list(data02yb))
data.dump(list(data02yc))
data.dump(list(data02yd))
data.dump(list(data02ye))
data.dump(list(data02yf))
data.dump(list(data02yg))

data.dump(list(data03x))
data.dump(list(data03ya))
data.dump(list(data03yb))
data.dump(list(data03yc))
data.dump(list(data03yd))
data.dump(list(data03ye))

data.dump(list(exercise02x))
data.dump(list(exercise02a))
data.dump(list(exercise02b))

data.dump(list(data04x))
data.dump(list(data04ya))
data.dump(list(data04yb))
data.dump(list(data04yc))
data.dump(list(data04yd))
data.dump(list(data04ye))

data.dump(list(data04u))
data.dump(list(data04v))

data.dump(list(data05x))
data.dump(list(data05y))

data.dump(list(data05half))
data.dump(list(data05quarter))

data.dump(list(data05xp))
data.dump(list(data05xm))
data.dump(list(data05yp))
data.dump(list(data05ym))

data.dump(exercise05n)
data.dump(list(exercise05x))
data.dump(list(exercise05y))
data.dump(list(exercise05y1))
data.dump(list(exercise05y2))
data.dump(list(exercise05y3))
data.dump(list(exercise05y4))

data.dump(data06n)
data.dump(list(data06t))
data.dump(list(data06r))

data.dump(exercise06n)
data.dump(list(exercise06t))
data.dump(list(exercise06r))

data.dump(data07n)
data.dump(list(data07))

data.dump(exercise07n)
data.dump(list(exercise07a))
data.dump(list(exercise07b))
data.dump(list(exercise07c))

data.dump(data08n)
data.dump(list(data08x))

data.dump(list(data08y))
data.dump(list(data08w))
data.dump(list(data08y1))
data.dump(list(data08y2))
data.dump(list(data08y3))

data.dump(exercise08n)
data.dump(list(exercise08x))

data.dump(list(exercise08y1a))
data.dump(list(exercise08y1b))

data.dump(list(exercise08y2a))
data.dump(list(exercise08y2b))

data.dump(list(exercise08y3a))
data.dump(list(exercise08y3b))

data.dump(list(exercise08y4a))
data.dump(list(exercise08y4b))


datafile.close()


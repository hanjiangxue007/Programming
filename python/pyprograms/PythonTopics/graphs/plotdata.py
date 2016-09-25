"""This module contains data for the UCS self-paced course on plotting
graphs with matplotlib.pyplot.  Having it avoids the need to explain
other data processing modules used to generate the data, helping the
student focus on the plotting aspects.

Bob Dowling <rjd4@cam.ac.uk>
2012
"""

import pickle

datafile = open('plotdata.pck', 'rb')
data = pickle.Unpickler(datafile)

# WARNING: Order of unpacking must match the order of packing in mkplotdata.py

data01x = data.load()
data01y = data.load()

exercise01x = data.load()
exercise01y = data.load()

data02x = data.load()
data02theta = data.load()

data02ya = data.load()
data02yb = data.load()
data02yc = data.load()
data02yd = data.load()
data02ye = data.load()
data02yf = data.load()
data02yg = data.load()

data03x = data.load()
data03ya = data.load()
data03yb = data.load()
data03yc = data.load()
data03yd = data.load()
data03ye = data.load()

exercise02x = data.load()
exercise02a = data.load()
exercise02b = data.load()

data04x = data.load()
data04ya = data.load()
data04yb = data.load()
data04yc = data.load()
data04yd = data.load()
data04ye = data.load()

data04u = data.load()
data04v = data.load()

data05x = data.load()
data05y = data.load()

data05half = data.load()
data05quarter = data.load()

data05xp = data.load()
data05xm = data.load()
data05yp = data.load()
data05ym = data.load()

exercise05n = data.load()
exercise05x = data.load()
exercise05y = data.load()
exercise05y1 = data.load()
exercise05y2 = data.load()
exercise05y3 = data.load()
exercise05y4 = data.load()

data06n = data.load()
data06t = data.load()
data06r = data.load()

exercise06n = data.load()
exercise06t = data.load()
exercise06r = data.load()

data07n = data.load()
data07  = data.load()

exercise07n = data.load()
exercise07a = data.load()
exercise07b = data.load()
exercise07c = data.load()

data08n = data.load()
data08x = data.load()

data08y = data.load()
data08w = data.load()
data08y1 = data.load()
data08y2 = data.load()
data08y3 = data.load()

exercise08n = data.load()
exercise08x = data.load()

exercise08y1a = data.load()
exercise08y1b = data.load()

exercise08y2a = data.load()
exercise08y2b = data.load()

exercise08y3a = data.load()
exercise08y3b = data.load()

exercise08y4a = data.load()
exercise08y4b = data.load()


datafile.close()
del datafile
del data

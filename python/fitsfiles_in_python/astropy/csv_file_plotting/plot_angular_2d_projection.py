#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Bhishan Poudel
# Date    : May 23, 2016

# Imports
from __future__ import division
from __future__ import print_function
from astropy.io import ascii
import numpy as np
import matplotlib.pyplot as plt

data = ascii.read("Young-Objects-Compilation.csv", header_start=1, data_start=2)


# As a final example, we will plot the angular positions from the catalog on a
# 2D projection of the sky. Instead of using pylab-style plotting,
# we'll take a more object-oriented approach.
# We'll start by creating a Figure object and adding a single subplot to the figure.
# We can specify a projection with the projection keyword; in this example we
# As a final example, we will plot the angular positions from the catalog on a
# 2D projection of the sky. Instead of using pylab-style plotting, we'll take a
# more object-oriented approach. We'll start by creating a Figure object
# and adding a single subplot to the figure. We can specify a projection with
# the projection keyword; in this example we will use a Mollweide projection.
# Unfortunately, it is highly non-trivial to make the matplotlib projection
# defined this way follow the celestial convention of longitude/RA increasing
# to the left.

# The axis object, ax, knows to expect angular coordinate values.
# An important fact is that it expects the values to be in radians, and it
# expects the azimuthal angle values to be between (-180º,180º).
# This is (currently) not customizable, so we have to coerce our RA data
# to conform to these rules! astropy provides a coordinate class for
# handling angular values, astropy.coordinates.Angle. We can convert our column
# of RA values to radians, and wrap the angle bounds using this class.

import astropy.coordinates as coord
import astropy.units as u

ra = coord.Angle(data['RA'].filled(np.nan)*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(data['Dec'].filled(np.nan)*u.degree)


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")

import astropy.coordinates as coord
import astropy.units as u
# ax.scatter(ra.radian, dec.radian)will use a Mollweide projection.
# Unfortunately, it is highly non-trivial to make the matplotlib projection
# defined this way follow the celestial convention of longitude/RA increasing
# to the left.

# The axis object, ax, knows to expect angular coordinate values.
# An important fact is that it expects the values to be in radians, and it
# expects the azimuthal angle values to be between (-180º,180º).
# This is (currently) not customizable, so we have to coerce our RA data
# to conform to these rules! astropy provides a coordinate class for
# handling angular values, astropy.coordinates.Angle. We can convert our column
# of RA values to radians, and wrap the angle bounds using this class.

import astropy.coordinates as coord
ra = coord.Angle(data['RA'].filled(np.nan)*u.degree)
ra = ra.wrap_at(180*u.degree)
dec = coord.Angle(data['Dec'].filled(np.nan)*u.degree)


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
#plt.show()


# By default, matplotlib will add degree ticklabels, so let's change the
# horizontal (x) tick labels to be in units of hours, and display a grid

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="mollweide")
ax.scatter(ra.radian, dec.radian)
ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
ax.grid(True)
#plt.show()

# We can save this figure as a PDF using the savefig function:

fig.savefig("map.pdf")

# Autogenerated by Astropy's setup.py on 2016-03-10 17:21:05.294529
from __future__ import unicode_literals
import datetime

version = "1.1.2"
githash = "e4e2951f278d667d48889cf0ed9077b9ae038a06"


major = 1
minor = 1
bugfix = 2

release = True
timestamp = datetime.datetime(2016, 3, 10, 17, 21, 5, 294529)
debug = False

try:
    from ._compiler import compiler
except ImportError:
    compiler = "unknown"

try:
    from .cython_version import cython_version
except ImportError:
    cython_version = "unknown"
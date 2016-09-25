#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author    : Bhishan Poudel 
# Date      : May 23, 2016 


# Imports
import pandas as pd

print(pd.__version__)

# For June 10, 2016, Answer = 0.18.0

# Pandas also provides a utility function, pd.show_versions(),
# which reports the version of its dependencies as well:

# after upgrading: 0.18.1


pd.show_versions()


# note for mac:
# i had python library default from Enthought canopy.
# from prefrence of Enthought i unset default python library
# restart the mac
# sudo -H pip install --upgrade pip
# sudo -H pip install --upgrade pandas

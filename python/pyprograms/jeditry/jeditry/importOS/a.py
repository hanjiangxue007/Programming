#! /usr/bin/env python

import os

for x in xrange(0, 12): # num_galaxies=12420
    postage_path = "%sstamp_%i"%("trial_0/",x)             # stamp_0 etc
    distorted_path = "%sdistorted_%i"%("trial_0/",x)       # distorted_0 etc
    if not os.path.exists(postage_path): os.makedirs(postage_path)
    if not os.path.exists(distorted_path): os.makedirs(distorted_path)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Oct-19-2016 Wed
# Last update :
#
#
# Imports
from __future__ import division, unicode_literals, print_function
from astropy.io import fits
import subprocess,os,time
from string import ascii_uppercase

_sim_feedme = 'sim.feedme'

def replace_galfit_param(name, value, object_num=1, fit=True):
    """
    Replaces a parameter value in the galfit configuration file.
    :param name: parameter name, without the following parenthesis
    :param value: new value for the parameter. Best provided as a string
    :param object_num: For object parameters, which object to change. Galfit
                   numbering, whichs starts with 1. Non-object params (e.g. B)
                   should use default object=1
    :param fit: Whether to fit the parameter (True) or hold fixed (False)
    """
    name, value = str(name), str(value)
    with open(_sim_feedme) as f:
        gf_file = f.readlines()
    # Control parameters only occur once, so 0th index is fine.
    loc = [i for i in range(len(gf_file)) if
           gf_file[i].strip().startswith(name+')')][object_num-1]
    param_str = gf_file[loc]
    comment = param_str.find('#')
    if name in ascii_uppercase:
        fmt = '{}) {} {}'
        param_str = fmt.format(name, value, param_str[comment:])
    else:
        fmt = '{}) {} {} {}'
        param_str = fmt.format(name, value, '0' if fit else '1',
                               param_str[comment:])
    gf_file[loc] = param_str
    with open(_sim_feedme, 'w') as f:
        f.writelines(gf_file)

if __name__ == '__main__':

    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()

    for i in list(range(2)):

        ingal = 'input_galaxies/gal{:d}.fits'.format(i)
        replace_galfit_param('A', ingal, object_num=1, fit=True)

        # run galfit
        cmd = 'galfit sim.feedme; rm -r galfit.01'
        subprocess.call(cmd,shell=True)

        # get model and residue
        model = 'galfit_outputs/gal_out{:d}.fits'.format(i)
        res   = 'galfit_outputs/gal_res{:d}.fits'.format(i)

        data1,header1 = fits.getdata(r"imgblock.fits", ext=2, header=True)
        data2,header2 = fits.getdata(r"imgblock.fits", ext=3, header=True)
        fits.writeto(model, data1, header1, clobber=True)
        fits.writeto(res, data2, header2, clobber=True)



    # print the time taken
    program_end_time = time.time()
    end_ctime        = time.ctime()
    seconds          = program_end_time - program_begin_time
    m, s             = divmod(seconds, 60)
    h, m             = divmod(m, 60)
    d, h             = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime,'\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

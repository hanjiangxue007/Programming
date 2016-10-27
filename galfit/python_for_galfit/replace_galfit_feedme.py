import numpy as np
import matplotlib.pyplot as pp
import os
import subprocess
from astropy.io import fits
from math import fsum
from scipy.ndimage import shift
from timeit import timeit
from string import ascii_uppercase

_sim_feedme = 'sim.feedme'
_sersic_ref_file = 'gfsim_n{:0.1f}.fits.gz'
_psf_ref_shift = np.array((2.2, 2.7))


def _replace_galfit_param(name, value, object_num=1, fit=True):
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
    name = '0'
    value = 'devauc'
    _replace_galfit_param(name, value, object_num=1, fit=True)

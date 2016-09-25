from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[ Extension("rbf",
              ["rbf.pyx"],
              libraries=["m"],
              extra_compile_args = ["-ffast-math"])]

setup(
  name = "rbf",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules)

# to compile: python setup.py build_ext --inplace
# gives: rbf.c and rbf.so

# test from ipython:
# from rbf import rbf_network
# %timeit rbf_network(X, beta, theta)


# comparison: 
# vanilla python : 7.67 seconds = 7670 ms
# cython         : 247 ms

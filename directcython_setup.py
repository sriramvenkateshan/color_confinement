from distutils.core import setup
from Cython.Build import cythonize
import numpy
import sys

setup(
    ext_modules = cythonize('directcython.pyx'),
    include_dirs = [numpy.get_include()]
)

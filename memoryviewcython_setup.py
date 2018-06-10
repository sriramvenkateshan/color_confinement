from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

sourcefiles = ['memoryviewcython.pyx', 'transform.c']
extensions = [Extension("memoryviewcython", sourcefiles)]

setup(
    ext_modules = cythonize(extensions),
    include_dirs = [numpy.get_include()]
)

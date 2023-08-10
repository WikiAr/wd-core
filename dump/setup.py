"""

python3 setup.py build_ext --inplace

"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='dump app',
    ext_modules = cythonize("/content/read_dump.pyx", compiler_directives={'language_level' : "3"})
)
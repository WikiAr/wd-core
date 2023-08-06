import os
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='dump app',
    ext_modules = cythonize("read_dump.py", compiler_directives={'language_level' : "3"})
)
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Integrate',
    ext_modules=cythonize("integr.pyx"),
    zip_safe=False,
)
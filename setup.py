"""Setup for deque.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov', 'tox']
}

setup(
    name='Data structures',
    description='Implements various data structures.',
    version='0.1',
    author='Chris Hudson, Morgan Nomura',
    author_email='c.ahudson84@yahoo.com, morganelle@gmail.com',
    license='MIT',
    py_modules=['deque'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)

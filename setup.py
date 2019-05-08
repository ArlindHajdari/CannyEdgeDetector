from setuptools import setup

setup(
    name = 'Canny edge detector',
    version = '0.1',
    description = 'An University task to create a canny edge detector app in python',
    author = 'XEK',
    url = '',
    license = 'UP',
    packages = ['CannyEdgeDetector'],
    entry_points = {'console_scripts': ['prog = main:main',],},
)
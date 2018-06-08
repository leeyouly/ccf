
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'ccf',
    version = '0.2.7',
    packages = find_packages(exclude=('tests','tests.*')),
    entry_points = {'scrapy': ['settings = ccf.settings']},
)
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='formatter-jamie-davis',
    version='0.1.0',
    description='Text formatting utility',
    long_description=readme,
    author='Jamie Davis',
    url='https://github.com/jamie-davis/formatter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
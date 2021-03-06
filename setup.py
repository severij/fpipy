#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'xarray',
    'rasterio',
    'colour_demosaicing',
    'configparser;python_version<"3.4"',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
    'flake8',
]

setup(
    name='fpipy',
    version='0.1.0',
    description='Tools for reading and manipulating raw data from\
    a Fabry-Perot interferometer based hyperspectral imager.',
    long_description=readme + '\n\n' + history,
    author="Matti A. Eskelinen",
    author_email='matti.a.eskelinen@student.jyu.fi',
    url='https://github.com/silmae/fpipy',
    packages=find_packages(include=['fpipy']),
    scripts=['bin/raw2rad'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='fpipy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'progressbar': ['tqdm'],
        },
    setup_requires=setup_requirements,
)

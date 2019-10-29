#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

setup(
    name="promregapi",
    version="0.1.0",  # Update also in __init__ ;
    description="Python API for Prometheus Registration",
    long_description="Simple wrapper for Prometheus Registration REST API",
    author="Henryk Iwaniuk",
    author_email="iwaniuk@tu-berlin.de",
    url='https://github.com/Teszko/promreg-api',
    license='https://raw.githubusercontent.com/Teszko/promreg-api/master/LICENSE',
    download_url='https://github.com/Teszko/promreg-api/releases/download/0.1/promreg-api-0.1.tar.gz',
    package_data={'': ['LICENSE', 'README.md']},
    packages=find_packages(),
    include_package_data=True,
    keywords='promreg prometheus',
    platforms='Posix; MacOS X; Windows',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)


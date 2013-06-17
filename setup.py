#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = [
    'requests==1.2.0',
]

setup(
    name='datatxt_querist',
    version='0.1',
    description='Simple library for extracting data from Wikipedia templates',
    author='Cristian Consonni',
    author_email='consonni@fbk.eu',
    url='https://github.com/SpazioDati/DataTXT-querist',
    packages= ['datatxt_querist'],
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)

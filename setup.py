#!/usr/bin/env python

from setuptools import setup
from codecs import open


with open('VERSION', encoding='utf-8') as version:
    ver = version.read().strip()

setup(
    name='scot-data',
    version=ver,
    description='Example data for the Source Connectivity Toolbox',
    url='https://github.com/scot-dev/scot-data',
    author='SCoT Development Team',
    author_email='scotdev@googlegroups.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='source connectivity EEG example data',
    packages=['scotdata'],
    package_data={'scotdata': ['*.mat']},
    install_requires=['scot', 'numpy']
)

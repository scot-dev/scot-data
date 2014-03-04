#!/usr/bin/env python

from distutils.core import setup


versionfile = open('VERSION', 'r')
ver = versionfile.read().strip()
versionfile.close()


setup(name='scot-data',
      version=ver,
      description='Example data for the Source Connectivity Toolbox',
      author='Martin Billinger',
      author_email='martin.billinger@tugraz.at',
      url='https://github.com/SCoT-dev/scot-data',
      packages=['scotdata'],
      package_data={'scotdata': ['*.mat']},
      
      install_requires=['scot']
     )


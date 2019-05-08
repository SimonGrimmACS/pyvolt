#!/usr/bin/env python

from setuptools import setup

setup(name='acs-state-estimation',
      version='0.1',
      description='State Estimation',
      author='Marco Pau, Markus Mirz, Jan Dinkelbach',
      author_email='acs-software@eonerc.rwth-aachen.de',
      packages = [ 'acs.state_estimation' ],
      install_requires = [
        'matplotlib',
        'numpy',
      ]
)
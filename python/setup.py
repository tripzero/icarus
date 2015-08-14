#!/usr/bin/env python

#someone always prefers setuptools over distutils.core
import os, json

#from distutils.core import setup #must import find_package, /usr/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'install_requires'
from distutils.core import setup

import setuptools

from os.path import join, dirname

#######################################################3
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

classifiers = [
			'Development Status :: 3 - Alpha',
	    	'Intended Audience :: Developers',
			'Programming Language :: Python :: 2',
	        'Programming Language :: Python :: 2.7'
		]

setup(
	    name = 'icarus',
	    author= 'Kevron Rees, Ryan Kapur',
	    author_email = 'kevron.rees@intel.com',
	    version = '1.1',
	    date_created = '6/19/2015',
	    long_description=read('../README.txt'),
	    packages = ['icarus'],
	    url = 'https://github.com/tripzero/mppt',
	    scripts = ['run_actuators.py'],
	    package_data={'': ['config.json']},
	    #'python.config.json',
	    license = 'Intel',

		requires = ['autobahn'],	
	)

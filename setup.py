# -*- coding:utf-8 -*-
#!/usr/bin/env python

from setuptools import setup

setup(
    name='httping',
    version='0.1',
    description='ping-like tool for pinging web servers via http',
    author='stone',
    author_email='stone4x4@gmail.com',
    url='http://github.com/stone/httping',
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Topic :: Internet",
      ],
      keywords='networking ping http internet',
      license='GPL',
      scripts=['httping.py']
     )

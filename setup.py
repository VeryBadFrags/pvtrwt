#!/usr/bin/env python3

from distutils.core import setup

setup(name='pvtrwt',
      version='0.2.0',
      description='Private Rewrite transforms YouTube and Twitter urls into their Invidio.us and Nitter.net equivalents.',
      long_description=open("README.md").read(),
      scripts=['pvtrwt'],

      author='VeryBadFrags',
      author_email='code@verybadfrags.com',
      url='https://github.com/VeryBadFrags/pvtrwt',

      licence="MIT"
      )

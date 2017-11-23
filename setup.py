#!/usr/bin/env python

from distutils.core import setup

try:
    readme = open('README', 'r')
    ldesc = readme.read(20000)
    readme.close()
except:
    ldesc = ""

setup(
    name='nxt-python2',
    version='2.2.2',
    author='Ryan B Au',
    author_email='auryan898@gmail.com',
    description='LEGO Mindstorms NXT Control Package',
    url='https://github.com/auryan898/nxt-python2',
    license='Gnu GPL v3',
    packages=['nxt', 'nxt.sensor'],
    scripts=['scripts/nxt_push', 'scripts/nxt_test', 'scripts/nxt_filer', 'scripts/nxt_server'],
    long_description=ldesc
)

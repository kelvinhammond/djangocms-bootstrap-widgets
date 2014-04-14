#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from bootstrap_widgets import __version__


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: Free for non-commercial use',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]


def read(fname):
    readme_file = os.path.join(os.path.dirname(__file__), fname)
    return os.popen(
        'which -s pandoc && pandoc -t rst {0} || cat {0}'
        .format(readme_file)).read()

setup(
    name='djangocms-bootstrap-widgets',
    version=__version__,
    description='Collection of plugins for DjangoCMS-Cascade to add widgets',
    author='Kelvin Hammond',
    author_email='hammond.kelvin@gmail.com',
    url='https://github.com/kelvinhammond/djangocms-bootstrap-widgets',
    packages=find_packages(exclude=['examples', 'docs']),
    install_requires=['djangocms-cascade'],
    license='LICENSE',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=read('README.md'),
    include_package_data=True,
    zip_safe=False
)

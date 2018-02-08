# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

import os
import io
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split('\n')


def long_description():
    """Load README.rst."""
    with open('README.rst', 'r') as f:
        return f.read()


setup(name='yamlloader',
      version='0.5.2',
      author='Jonas Eschle "Mayou36"',
      author_email='jonas.eschle@phynix.science',
      maintainer='Jonas Eschle "Mayou36"',
      maintainer_email='jonas.eschle@phynix.science',
      url='https://github.com/Phynix/yamlloader',
      download_url='https://github.com/Phynix/yamlloader',
      license='MIT License',
      description='YAML loader and dumper for PyYAML allowing to keep keys order.',
      long_description=long_description(),
      keywords=['YAML', 'loader', 'dumper', 'ordered', 'OrderedDict', 'pyyaml'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators', 'Natural Language :: English',
                   'License :: OSI Approved :: MIT License', 'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6', 'Topic :: Utilities'],
      packages=['yamlloader', 'yamlloader.ordereddict'],
      python_requires=">=2.7",
      install_requires=requirements,
      zip_safe=False
      )

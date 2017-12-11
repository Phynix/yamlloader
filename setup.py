# -*- coding: utf-8 -*-


import sys
from setuptools import setup

requires = ['pyyaml']
if float('{:d}.{:d}'.format(*sys.version_info[:2])) < 2.7:
    requires.append('ordereddict')

def long_description():
    with open('README.rst', 'r') as f:
        return f.read()

setup(
    name='yamlloader',
    version='0.4.1',
    author='Jonas Eschle',  # 'François Ménabé',
    author_email='jonas.eschle@phynix.science',  # 'francois.menabe@gmail.com',
    url='https://github.com/Phynix/yamlloader',
    download_url='https://github.com/Phynix/yamlloader',
    license='MIT License',
    description='YAML loader and dumper for PyYAML allowing to keep keys order.',
    long_description=long_description(),
    keywords=['YAML', 'loader', 'dumper', 'ordered', 'OrderedDict', 'pyyaml'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Intended Audience :: System Administrators',
                 'Natural Language :: English',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Utilities'],
    packages=['yamlloader'],
    install_requires=requires)

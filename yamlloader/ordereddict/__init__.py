# -*- coding: utf-8 -*-
"""YAML loaders and dumpers for PyYAML allowing to keep keys order."""
from __future__ import print_function, division, absolute_import

from .loaders import Loader, SafeLoader
from .dumpers import Dumper, SafeDumper

__c_handler_names = []

try:
    from .loaders import CLoader, CSafeLoader
    from .dumpers import CDumper, CSafeDumper
    __c_handler_names += ['CLoader',
                          'CDumper',
                          'CSafeLoader',
                          'CSafeDumper',
                          ]
except ImportError:  # PyYAML.cyaml not available -> error
    pass  # C version not available

__all__ = ['Loader',
           'Dumper',
           'SafeLoader',
           'SafeDumper'] + __c_handler_names

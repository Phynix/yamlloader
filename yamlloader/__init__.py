"""
Several different loaders and dumpers for YAML under Python are implemented in the
respective submodules.


"""

from __future__ import print_function, division, absolute_import

import sys

__version__ = "0.4.1"
__author__ = "Jonas Eschle"
__email__ = "jonas.eschle@phynix.science"

from . import ordereddict

if sys.version_info[:2] < (2, 7):
    raise RuntimeError("You are using Python < 2.7. This is not supported. "
                       "Please upgrade your distribution and/or packages.")

__all__ = ['ordereddict']

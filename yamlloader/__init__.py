from __future__ import print_function, division, absolute_import

import sys

__author__ = "Jonas Eschle"
__email__ = "jonas.eschle@phynix.science"

if sys.version_info[:2] < (2, 7):
    raise RuntimeError("You are using Python < 2.7. This is not supported. "
                       "Please upgrade your distribution and/or packages.")

from . import ordereddict

"""
Global settings for the behavior of the module.


"""

from __future__ import print_function, division, absolute_import

import sys

ALLOW_NON_C_FALLBACK = True

PY_GE_37 = (sys.version_info.major >= 3 and sys.version_info.minor >= 7) or sys.version_info >= 4


"""Test that the C version fallback/fail works for PyYAML cyaml."""
from __future__ import print_function, division, absolute_import

from unittest import TestCase


class TestCVersionHandling(TestCase):

    def test_c_fallback(self):
        import yamlloader

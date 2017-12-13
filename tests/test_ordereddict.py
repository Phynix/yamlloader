from __future__ import print_function, division, absolute_import

import contextlib
import tempfile
import copy
import os
from collections import OrderedDict
from unittest import TestCase

import atexit

import hypothesis
from hypothesis import given, settings
import hypothesis.strategies as st
import yaml

import yamlloader

# long_settings = settings(max_examples=10, max_iterations=20, max_shrinks=10)
long_settings = settings(max_examples=100, max_iterations=200, max_shrinks=100)


# long_settings = settings(max_examples=1000, max_iterations=2000, max_shrinks=1000,
#                          timeout=hypothesis.unlimited)


def create_tempfile(suffix=None):
    """Create a temporary file and remove it on exit "guaranteed".

    Returns:
        tuple(os handle, str): Returns same objects as :py:func:`tempfile.mkstemp`.
    """

    try:
        os_handle, filename = tempfile.mkstemp(suffix=suffix)
    except Exception:  # aiming at interruptions
        print("Exception occurred while creating a temp-file")
        raise
    finally:
        atexit.register(cleanup_file, filename)

    return os_handle, filename


def cleanup_file(filename):
    """Remove a file if exists."""
    try:
        os.remove(filename)
    except FileNotFoundError as error:
        pass  # file was not created at all


@contextlib.contextmanager
def temp_file():
    """Create temporary files, cleanup after exit"""
    _, file_name = create_tempfile()
    yield file_name
    os.remove(file_name)


dict_keys_strat = st.text(average_size=6, min_size=1, max_size=25)
dict_val_strat = st.one_of(st.text(average_size=10, min_size=1, max_size=10000), st.integers(),
                           st.floats(allow_nan=False, allow_infinity=False),
                           st.lists(st.one_of(st.text(max_size=10),
                                              st.floats(allow_nan=False, allow_infinity=False),
                                              st.integers())))


def extend_dict(strategy):
    new_dict = st.dictionaries(keys=copy.deepcopy(dict_keys_strat),
                               values=strategy, dict_class=OrderedDict)
    return new_dict


recursive_dict_strat = st.recursive(base=st.dictionaries(keys=copy.deepcopy(dict_keys_strat),
                                                         values=copy.deepcopy(dict_val_strat),
                                                         dict_class=OrderedDict),
                                    extend=extend_dict, max_leaves=30)
loaders = [yamlloader.ordereddict.Loader, yamlloader.ordereddict.SafeLoader]
dumpers = [yamlloader.ordereddict.Dumper, yamlloader.ordereddict.SafeDumper]

class TestLoaderDumper(TestCase):

    # def test_normalLoaderDumper(self):
    #     self.loader = yamlloader.ordereddict.Loader
    #     self.dumper = yamlloader.ordereddict.Dumper
    #     self.loaddump()
    #
    # def test_SafeLoaderDumper(self):
    #     self.loader = yamlloader.ordereddict.SafeLoader
    #     self.dumper = yamlloader.ordereddict.SafeDumper
    #     self.loaddump()

    def set_LoadersDumbers(self, loader, dumper):
        self.loader = loader
        self.dumper = dumper

    def test_SafeLoadCombinations(self):
        for dumper in dumpers:
            for loader in loaders:
                self.set_LoadersDumbers(loader=loader, dumper=dumper)
                self.loaddump()

    # def test_normalCLoaderCDumper(self):
    #     self.loader = yamlloader.ordereddict.CLoader
    #     self.dumper = yamlloader.ordereddict.CDumper
    #     self.loaddump()

    @long_settings
    @given(recursive_dict_strat)
    def loaddump(self, dict_to_save):
        # with temp_file() as tfile_name:
        #     with open(tfile_name, mode='w') as tfile_write:
        #         yaml.dump(dict_to_save, tfile_write, dumper)
        #
        #     with open(tfile_name, mode='r') as tfile_read:
        #         dict_loaded = yaml.load(tfile_read, loader)
        dumbed_dict = yaml.dump(dict_to_save, Dumper=self.dumper)
        dict_loaded = yaml.load(dumbed_dict, Loader=self.loader)
        self.assertEqual(dict_to_save, dict_loaded)


class TestAssumptions(TestCase):

    def setUp(self):
        self.odict1 = OrderedDict(
                [('a', [11, 12, 13]), ('b', [21, 22, 23]), ('c', [31, 32, 33]), ('e', [21, 22, 23]),
                 ('d', [11, 12, 13]), ('f', OrderedDict(
                        [('a', [11, 12, 13]), ('b', [21, 22, 23]), ('c', [31, 32, 33]),
                         ('e', [21, 22, 23]), ('d', [11, 12, 13])]))])
        self.odict2 = OrderedDict(
                [('a', [11, 12, 13]), ('b', [21, 22, 23]), ('c', [31, 32, 33]), ('e', [21, 22, 23]),
                 ('d', [11, 12, 13]), ('f', OrderedDict(
                        [('a', [11, 12, 13]), ('b', [21, 22, 23]), ('c', [31, 32, 33]),
                         ('d', [11, 12, 13]), ('e', [21, 22, 23])]))])

    def test_equality_assumptions(self):
        self.assertNotEqual(self.odict1, self.odict2)
        self.assertEqual(self.odict2, self.odict2)
        self.assertEqual(self.odict2, copy.deepcopy(self.odict2))

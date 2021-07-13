import copy
from collections import OrderedDict
from unittest import TestCase

import hypothesis
import hypothesis.strategies as st
import yaml
from hypothesis import given, settings, HealthCheck

import yamlloader

ASCII_CODEPOINT = 126

long_settings = settings(
    max_examples=20,
    suppress_health_check=(HealthCheck.too_slow, HealthCheck.data_too_large),
)


def dict_keys_strat(ascii_only=False):
    blacklist_characters = []
    if ascii_only:
        max_codepoint = ASCII_CODEPOINT
        blacklist_characters = ["u", "'", '"']
    else:
        max_codepoint = None
    return st.text(
        alphabet=st.characters(
            max_codepoint=max_codepoint, blacklist_characters=blacklist_characters
        ),
        # avoid u'str'!
        min_size=1,
        max_size=25,
    )


def dict_val_strat(ascii_only=False):
    blacklist_characters = []
    if ascii_only:
        max_codepoint = ASCII_CODEPOINT
        blacklist_characters = ["u", "'", '"']
    else:
        max_codepoint = None
    text = st.text(
        alphabet=st.characters(
            max_codepoint=max_codepoint, blacklist_characters=blacklist_characters
        ),
        # avoid u'str'!
        min_size=100,
        max_size=10000,
    )
    return st.one_of(
        text,
        st.integers(),
        st.floats(allow_nan=False, allow_infinity=False),
        st.lists(
            st.one_of(
                st.text(max_size=10),
                st.floats(allow_nan=False, allow_infinity=False),
                st.integers(),
            )
        ),
    )


def get_extended_dict(ascii_only=False, dict_class=None):
    def extend_dict(strategy):
        new_dict = st.dictionaries(
            keys=copy.deepcopy(dict_keys_strat(ascii_only=ascii_only)),
            values=strategy,
            dict_class=dict_class,
        )
        return new_dict

    return extend_dict


def recursive_dict_strat(ascii_only=False, dict_class=None):
    return st.recursive(
        base=st.dictionaries(
            keys=copy.deepcopy(dict_keys_strat(ascii_only=ascii_only)),
            values=copy.deepcopy(dict_val_strat(ascii_only=ascii_only)),
            dict_class=dict_class,
        ),
        extend=get_extended_dict(ascii_only=ascii_only, dict_class=dict_class),
        max_leaves=5,
    )


loaders = [
    yamlloader.ordereddict.Loader,
    yamlloader.ordereddict.SafeLoader,
    yamlloader.ordereddict.CLoader,
    yamlloader.ordereddict.CSafeLoader,
]
dumpers = [
    yamlloader.ordereddict.Dumper,
    yamlloader.ordereddict.SafeDumper,
    yamlloader.ordereddict.CDumper,
    yamlloader.ordereddict.CSafeDumper,
]

yaml_loaders = {
    yamlloader.ordereddict.Loader: yaml.Loader,
    yamlloader.ordereddict.SafeLoader: yaml.SafeLoader,
    yamlloader.ordereddict.CLoader: yaml.CLoader,
    yamlloader.ordereddict.CSafeLoader: yaml.CSafeLoader,
}

yaml_dumpers = {
    yamlloader.ordereddict.Dumper: yaml.Dumper,
    yamlloader.ordereddict.SafeDumper: yaml.SafeDumper,
    yamlloader.ordereddict.CDumper: yaml.CDumper,
    yamlloader.ordereddict.CSafeDumper: yaml.CSafeDumper,
}

safe_loaders = [yamlloader.ordereddict.SafeLoader, yamlloader.ordereddict.CSafeLoader]
safe_dumpers = [yamlloader.ordereddict.SafeDumper, yamlloader.ordereddict.CSafeDumper]

loaderdumper = [(l, d) for l in loaders for d in dumpers]


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

    def set_LoadersDumpers(self, loader, dumper):
        self.loader = loader
        self.dumper = dumper

    def test_SafeLoadCombinations(self):
        for loader, dumper in loaderdumper:
            self.set_LoadersDumpers(loader=loader, dumper=dumper)

            self.loaddump_unicode()

    def loaddump_ascii_only(self):

        self.loaddump_ascii_only_pyle36()

    @long_settings
    @given(recursive_dict_strat(ascii_only=True, dict_class=OrderedDict))
    def loaddump_ascii_only_pyle36(self, dict_to_save):
        self._load_dump_ascii_only(dict_to_save)

    def _load_dump_ascii_only(self, dict_to_save):
        if self.loader in safe_loaders and self.dumper not in safe_dumpers:
            return
        try:
            dumbed_dict = yaml.dump(
                dict(dict_to_save), Dumper=yaml_dumpers[self.dumper]
            )
            dict_loaded = yaml.load(dumbed_dict, Loader=yaml_loaders[self.loader])
            hypothesis.assume(dict(dict_to_save) == dict_loaded)
        except UnicodeError:
            print("Problems with unicode in SafeLoaders")
            # hypothesis.assume(False)
        self.loaddump(dict_to_save=dict_to_save)

    def loaddump_unicode(self):
        self.loaddump_unicode_pyle36()

    @long_settings
    @given(recursive_dict_strat(dict_class=OrderedDict))
    def loaddump_unicode_pyle36(self, dict_to_save):
        self._loaddump_unicode(dict_to_save=dict_to_save)

    def _loaddump_unicode(self, dict_to_save):
        def convert_nested_dict(dictionary, convert_from=None, convert_to=dict):
            new_dict = {}
            for key, val in dictionary.items():
                if isinstance(val, convert_from):
                    val = convert_to(val)
                if isinstance(val, dict):
                    val = convert_nested_dict(
                        dictionary=val, convert_from=convert_from, convert_to=convert_to
                    )
                new_dict[key] = val
            return new_dict

        dict_conv_to_save = convert_nested_dict(
            dict_to_save, convert_from=(OrderedDict, dict), convert_to=dict
        )
        # Test if dumping with yaml normally is possible
        try:
            dumbed_dict = yaml.dump(dict_conv_to_save, Dumper=yaml_dumpers[self.dumper])
            dict_loaded = yaml.load(dumbed_dict, Loader=yaml_loaders[self.loader])
            hypothesis.assume(dict_conv_to_save == dict_loaded)
            # self.assertEqual(dict(dict_to_save), dict_loaded)
        except UnicodeError:
            print("Problems with unicode and original yaml Dumpers")
            hypothesis.assume(False)
        except yaml.scanner.ScannerError as error:
            print("Problems with scanning in original yaml Dumpers: ", error)
            hypothesis.assume(False)
        self.loaddump(dict_to_save=dict_to_save)

    def loaddump(self, dict_to_save, loader=None, dumper=None):
        if loader is None:
            loader = self.loader
        if dumper is None:
            dumper = self.dumper
        dumbed_dict = yaml.dump(dict_to_save, Dumper=dumper)
        dict_loaded = yaml.load(dumbed_dict, Loader=loader)
        self.assertEqual(dict_to_save, dict_loaded)
        self.assertListEqual(list(dict_to_save.keys()), list(dict_loaded.keys()))
        self.assertEqual(type(dict_to_save), type(dict_loaded))


class TestAssumptions(TestCase):
    def setUp(self):
        self.odict1 = OrderedDict(
            [
                ("a", [11, 12, 13]),
                ("b", [21, 22, 23]),
                ("c", [31, 32, 33]),
                ("e", [21, 22, 23]),
                ("d", [11, 12, 13]),
                (
                    "f",
                    OrderedDict(
                        [
                            ("a", [11, 12, 13]),
                            ("b", [21, 22, 23]),
                            ("c", [31, 32, 33]),
                            ("e", [21, 22, 23]),
                            ("d", [11, 12, 13]),
                        ]
                    ),
                ),
            ]
        )
        self.odict2 = OrderedDict(
            [
                ("a", [11, 12, 13]),
                ("b", [21, 22, 23]),
                ("c", [31, 32, 33]),
                ("e", [21, 22, 23]),
                ("d", [11, 12, 13]),
                (
                    "f",
                    OrderedDict(
                        [
                            ("a", [11, 12, 13]),
                            ("b", [21, 22, 23]),
                            ("c", [31, 32, 33]),
                            ("d", [11, 12, 13]),
                            ("e", [21, 22, 23]),
                        ]
                    ),
                ),
            ]
        )

    def test_equality_assumptions(self):
        self.assertNotEqual(self.odict1, self.odict2)
        self.assertEqual(self.odict2, self.odict2)
        self.assertEqual(self.odict2, copy.deepcopy(self.odict2))

import yaml

from collections import OrderedDict


def represent_ordereddict(self, data):
    return self.represent_mapping('tag:yaml.org,2002:map', data.items())


class OrderedDumperMixin(object):
    def __init__(self, *args, **kwargs):
        super(OrderedDumperMixin, self).__init__(*args, **kwargs)
        self.add_representer(OrderedDict, type(self).represent_ordereddict)

    represent_ordereddict = represent_ordereddict


class Dumper(OrderedDumperMixin, yaml.Dumper):
    pass


class SafeDumper(OrderedDumperMixin, yaml.SafeDumper):
    pass


class CDumper(OrderedDumperMixin, yaml.CDumper):
    pass


class CSafeDumper(OrderedDumperMixin, yaml.CSafeDumper):
    pass

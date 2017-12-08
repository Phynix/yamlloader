yamlloader
==========

This project was mirrored from `yamlordereddict <https://github.com/fmenabe/python-yamlordereddictloader>_
Many thanks to the original author François Ménabé!



This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict loader/dumper is
 implemented, allowing to keep items order
when loading resp. dumping a file.


To install it
-------------

.. code-block:: bash

    $ pip install yamlloader

Loader usage
------------

.. code-block:: python

    import yaml
    import yamlloader

    data = yaml.load(open('myfile.yml'), Loader=yamlloader.ordereddict.CLoader)  # CLoader is faster than Loader

**Note:** For using the safe loader (which takes standard YAML tags and does
not construct arbitrary Python objects), replace ``yamlorderdictloader.CLoader`` by
``yamlorderedictloader.CSafeLoader``.

Dumper usage
------------

.. code-block:: python

    import yaml
    import yamlloader
    from collections import OrderedDict

    data = OrderedDict([
        ('key1', 'val1'),
        ('key2', OrderedDict([('key21', 'val21'), ('key22', 'val22')]))
    ])
    yaml.dump(data,
              open('myfile.yml', 'w'),
              Dumper=yamlloader.ordereddict.CDumper,
              default_flow_style=False)

**Note:** For using the safe dumper (which produce standard YAML tags and does
not represent arbitrary Python objects), replace ``yamlorderdictloader.Dumper`` by
``yamlorderedictloader.SafeDumper``.

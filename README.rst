.. image:: https://travis-ci.org/Phynix/yamlloader.svg?branch=master
    :target: https://travis-ci.org/Phynix/yamlloader
.. image:: https://landscape.io/github/Phynix/yamlloader/master/landscape.svg?style=flat
    :target: https://landscape.io/github/Phynix/yamlloader/master
    :alt: Code Health
.. image:: https://www.versioneye.com/user/projects/5a2f00060fb24f07e40988bf/badge.svg?style=flat-square
    :target: https://www.versioneye.com/user/projects/5a2f00060fb24f07e40988bf
    :alt: Dependency Status
.. image:: https://coveralls.io/repos/github/Phynix/yamlloader/badge.svg
    :target: https://coveralls.io/github/Phynix/yamlloader

yamlloader
==========


This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict loader/dumper is
implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict.

This project was originally mirrored from
`yamlordereddict <https://github.com/fmenabe/python-yamlordereddictloader>`_
Many thanks to the original author François Ménabé!
The library contains several improvements including automated testing and
 the much faster C-versions of the Loaders/Dumpers.


`API Documentation <https://phynix.github.io/yamlloader/index.html>`_


Install
-------
It is recommended to use the pip or anaconda version

.. code-block:: bash

    $ pip install yamlloader

or

.. code-block:: bash

    $ conda install yamlloader -c phynix


But does [your special case here] also work?
--------------------------------------------

Tests are run continuously using randomly generated yaml files.
Also, there are no fails to be expected.

Still, if you are concerned that *your* special case may breaks in the future, please
add your own tests as `test_ext_anyname.py` under `tests/` or let us know about your needs.
This guarantees that no code will be added that breaks *your* case.


Loader usage
------------

.. code-block:: python

    import yaml
    import yamlloader

    with open('myfile.yml') as yaml_file:
        data = yaml.load(yaml_file,
                         Loader=yamlloader.ordereddict.CLoader)
                         # CLoader is faster than Loader

**Note:** For using the safe loader (which takes standard YAML tags and does
not construct arbitrary Python objects), replace ``yamlloader.ordereddict.CLoader`` by
``yamlloader.ordereddict.CSafeLoader``.

Dumper usage
------------

.. code-block:: python

    import yaml
    import yamlloader
    from collections import OrderedDict

    data = OrderedDict([('key1', 'val1'),
                        ('key2', OrderedDict([('key21', 'val21'),
                                              ('key22', 'val22')]))])

    with open('myfile.yaml', 'w') as yaml_file:
        yaml.dump(data, yaml_file,
                  Dumper=yamlloader.ordereddict.CDumper)

**Note:** For using the safe dumper (which produce standard YAML tags and does
not represent arbitrary Python objects), replace ``yamlloader.ordereddict.CDumper`` by
``yamlloader.ordereddict.CSafeDumper``.

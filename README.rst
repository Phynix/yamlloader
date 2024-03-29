
.. image:: https://github.com/Phynix/yamlloader/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/Phynix/yamlloader/actions
.. image:: https://img.shields.io/pypi/pyversions/yamlloader.svg
    :target: https://pypi.org/project/yamlloader/
.. image:: https://badge.fury.io/py/yamlloader.svg
    :target: https://badge.fury.io/py/yamlloader
.. image:: https://coveralls.io/repos/github/Phynix/yamlloader/badge.svg
    :target: https://coveralls.io/github/Phynix/yamlloader

yamlloader
==========


This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict loader/dumper is
implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (Python 3.7+: Also regular dicts are supported and are the default items to be loaded to. As of Python 3.7 preservation of insertion order is a language feature of regular dicts.)

This project was originally mirrored from
`yamlordereddict <https://github.com/fmenabe/python-yamlordereddictloader>`_
Many thanks to the original author François Ménabé!
The library contains several improvements including automated testing and
the much faster C-versions of the Loaders/Dumpers.


`API Documentation <https://yamlloader.readthedocs.io/>`_


Install
-------
There is a pip and a conda version available

.. code-block:: bash

    $ pip install yamlloader

or

.. code-block:: bash

    $ conda install yamlloader -c conda-forge


But does [your special case here] also work?
--------------------------------------------

Tests are run continuously using randomly generated yaml files.
Also, there are no fails to be expected.

Still, if you are concerned that *your* special case may breaks in the future, please
add your own tests as `test_ext_anyname.py` under `tests/` or let us know about your needs.
This guarantees that no code will be added that breaks *your* case.


C vs non-C version
------------------

A significant speedup can be reached by replacing the Loader* and Dumper* classes by CLoader*
and CDumper*. The package hereby relies on the implementations from PyYAML. If they have not
been compiled, *yamlloader* **automatically** falls back to the non-C versions.

Therefore using the C-version is safe: if it is not available, the pure Python version is
automatically used.

Usage examples
==============


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


FAQ
===

C version not working
---------------------------
If the C version is not working (it falls back by default to a non-C version),
check if yaml.cyaml exists. If not, the cyaml module was not compiled during the installation of
yaml (pyyaml). Make sure that cython is installed (`pip install Cython`) and the yaml.h file is
there (apt: libyaml-dev).

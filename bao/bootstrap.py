# coding: utf-8
"""Bootstrap utilites for bao.

If bao was not installed through Pip, bao can install itself using its own package.
Packages generated by bao can be importable as a namespace (by adding the zip path to sys.path.)
So, this is possible:

>>> import sys
>>> sys.path.insert(-1, "/path/to/bao/zip")
>>> import bao.concrete
>>> bao.concrete.install("/path/to/bao/zip")

Or shorter (this module does all of it for you):

>>> import bao
>>> bao.bootstrap()

Pip also bootstraps pretty much the same way.
Bootstrapping is only supported if bao was not installed through Pip.
"""

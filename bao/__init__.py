# coding: utf8
"""bao: pure-Python port of LibTerm's 'package.swift' command.

Features:
- External repo support.
- Backward-compatibility with the 'package' command. By accessing the UserDefaults plist file, packages installed by the 'package' command will appear in picaro, and vice versa.
- Package builder: Create a package out of a script automatically.

The backend for bao data serialization is by default TOML.
"""

import os
import sys

__author__ = "Ong Yong Xin"
__copyright__ = "Copyright 2020, Ong Yong Xin"
__credits__ = ["Ong Yong Xin"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ong Yong Xin"
__email__ = "ongyongxin2020+github@gmail.com"
__status__ = "Prototype"

VERSION_REQUIRED = (3, 6)
ENABLE_PLATFORM_CHECK = False  # disable for debugging

if not sys.version_info >= VERSION_REQUIRED:
    raise NotImplementedError(
        f"you must have at least Python {'.'.join(str(v) for v in VERSION_REQUIRED)}"
    )

if ENABLE_PLATFORM_CHECK:
    # use XPC service ID to check
    if "ch.marcela.ada.LibTerm" not in os.getenv("XPC_SERVICE_NAME"):
        raise NotImplementedError("Only LibTerm is supported now, sorry :(")


# don't muck up the namespace
del os, sys
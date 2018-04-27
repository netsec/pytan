"""A python package that makes using the Tanium Server SOAP API easy."""
import logging
import os
import sys

__title__ = 'PyTan'
__version__ = '2.2.3'
"""
Version of PyTan
"""

__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
"""
Author of Pytan
"""

__license__ = 'MIT'
"""
License for PyTan
"""

__copyright__ = 'Copyright 2015 Tanium'
"""
Copyright for PyTan
"""

# disable python from creating .pyc files everywhere
sys.dont_write_bytecode = True

my_file = os.path.abspath(__file__)
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
path_adds = [parent_dir]
[sys.path.insert(0, aa) for aa in path_adds]

try:
    import libs_external  # noqa
except Exception:
    pass

try:
    import taniumpy  # noqa

    import pytan  # noqa
    import pytan.utils  # noqa
    import pytan.constants  # noqa
    import pytan.exceptions  # noqa
    import pytan.handler  # noqa
    import pytan.help  # noqa
    import pytan.sessions  # noqa
    import pytan.xml_clean  # noqa

    from pytan import arg_tools  # noqa
    from pytan import constants  # noqa
    from pytan import exceptions  # noqa
    from pytan import help  # noqa
    from pytan import pollers  # noqa
    from pytan import sessions  # noqa
    from pytan import utils  # noqa

    from pytan.handler import Handler  # noqa
except Exception:
    raise

# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):  # noqa
        def emit(self, record):  # noqa
            pass

logging.getLogger(__name__).addHandler(NullHandler())

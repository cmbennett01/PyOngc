# SPDX-FileCopyrightText: 2017 Mattia Verga <mattia.verga@tiscali.it>
#
# SPDX-License-Identifier: MIT

"""Python interface to OpenNGC database data."""

from importlib.metadata import version

__version__ = version('PyOngc')

try:
    from importlib.resources import files
    DBPATH = str(files(__name__) / 'ongc.db')
except ImportError:
    from pkg_resources import resource_filename
    DBPATH = resource_filename(__name__, 'ongc.db')

DBDATE = 20221023  # Version of database data

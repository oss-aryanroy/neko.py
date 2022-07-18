"""
NekoBot API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the NekoBot API.
:copyright: (c) 2022-present Bur-ham
:license: MIT, see LICENSE for more details.
"""

from typing import Literal, NamedTuple

from .api import *
from .errors import *

__title__ = 'neko'
__author__ = 'Bur-ham'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present Bur-ham'
__version__ = '1.0.0'


class Version(NamedTuple):
    major: int
    minor: int
    micro: int
    release: Literal['alpha', 'beta', 'stable', 'final']

version = Version(1, 0, 0, 'final')



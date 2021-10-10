# -*- coding: utf-8 -*-

__author__ = "Donatus Herre <donatus.herre@slub-dresden.de>"
__version__ = "2021.10.10"
__license__ = "GPLv3"

from .repos import Digital, Qucosa
from .store import write, write_pretty

digital = Digital()
qucosa = Qucosa()

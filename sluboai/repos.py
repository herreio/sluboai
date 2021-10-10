# -*- coding: utf-8 -*-

from .base import Client


class Qucosa(Client):

    def __init__(self):
        super().__init__("https://slub.qucosa.de/oai/")


class Digital(Client):

    def __init__(self):
        super().__init__("https://digital.slub-dresden.de/oai")

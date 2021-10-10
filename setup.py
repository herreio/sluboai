# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="sluboai",
    version="2021.10.10",
    author="Donatus Herre",
    author_email="donatus.herre@slub-dresden.de",
    description="Client for OAI-PMH respositories of SLUB Dresden",
    license=open("LICENSE").read(),
    url="https://github.com/herreio/sluboai",
    packages=["sluboai"],
    install_requires=["sickle"],
)

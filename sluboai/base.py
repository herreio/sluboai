# -*- coding: utf-8 -*-

from sickle import Sickle


class Client:

    def __init__(self, url):
        self.pmh = Sickle(url)
        self.formats = [mdf.metadataPrefix
                        for mdf in self.pmh.ListMetadataFormats()]
        self.sets = {oai_set.setSpec: oai_set.setName
                     for oai_set in self.pmh.ListSets()}

    def record(self, oai_id, schema="oai_dc"):
        if schema not in self.formats:
            return None
        return self.pmh.GetRecord(identifier=oai_id, metadataPrefix=schema)

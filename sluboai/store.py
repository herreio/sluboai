# -*- coding: utf-8 -*-

from lxml import etree


def write(res, path):
    with open(path, "w", encoding="utf-8") as f:
        if hasattr(res, "raw"):
            f.write(res.raw)
        elif hasattr(res, "oai_response"):
            f.write(res.oai_response.raw)


def write_pretty(res, path):
    xml_tree = None
    if hasattr(res, "xml"):
        xml_tree = etree.ElementTree(res.xml)
    elif hasattr(res, "oai_response"):
        xml_tree = etree.ElementTree(res.oai_response.xml)
    if xml_tree is not None:
        xml_tree.write(path, xml_declaration=True,
                       encoding="UTF-8", pretty_print=True)

import sluboai
import unittest


class TestWriteIdentify(unittest.TestCase):

    def test_digital(self):
        digital_identify = sluboai.digital.pmh.Identify()
        sluboai.write(digital_identify, "test/write/digital_identify.xml")
        sluboai.write_pretty(digital_identify, "test/write/digital_identify_pretty.xml")

    def test_qucosa(self):
        qucosa_identify = sluboai.qucosa.pmh.Identify()
        sluboai.write(qucosa_identify, "test/write/qucosa_identify.xml")
        sluboai.write_pretty(qucosa_identify, "test/write/qucosa_identify_pretty.xml")


class TestWriteMdFormats(unittest.TestCase):

    def test_digital(self):
        digital_mdformats = sluboai.digital.pmh.ListMetadataFormats()
        sluboai.write(digital_mdformats, "test/write/digital_list_metadata_formats.xml")
        sluboai.write_pretty(digital_mdformats, "test/write/digital_list_metadata_formats_pretty.xml")

    def test_qucosa(self):
        qucosa_mdformats = sluboai.qucosa.pmh.ListMetadataFormats()
        sluboai.write(qucosa_mdformats, "test/write/qucosa_list_metadata_formats.xml")
        sluboai.write_pretty(qucosa_mdformats, "test/write/qucosa_list_metadata_formats_pretty.xml")


class TestWriteSets(unittest.TestCase):

    def test_digital(self):
        digital_sets = sluboai.digital.pmh.ListSets()
        sluboai.write(digital_sets, "test/write/digital_list_sets.xml")
        sluboai.write_pretty(digital_sets, "test/write/digital_list_sets_pretty.xml")

    def test_qucosa(self):
        qucosa_sets = sluboai.qucosa.pmh.ListSets()
        sluboai.write(qucosa_sets, "test/write/qucosa_list_sets.xml")
        sluboai.write_pretty(qucosa_sets, "test/write/qucosa_list_sets_pretty.xml")


if __name__ == '__main__':
    unittest.main()

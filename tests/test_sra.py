from unittest import TestCase
from isatools import isajson, sra
from lxml import etree
import os
import shutil
from tests import utils
import tempfile


def setUpModule():
    if not os.path.exists(utils.DATA_DIR):
        raise FileNotFoundError("Could not fine test data directory in {0}. Ensure you have cloned the ISAdatasets "
                                "repository using "
                                "git clone -b tests --single-branch git@github.com:ISA-tools/ISAdatasets {0}"
                                .format(utils.DATA_DIR))


class TestNewSraExport(TestCase):

    # TODO: Isolate testing SRA writer (don't rely on ISA JSON loader)

    def setUp(self):

        self._json_data_dir = utils.JSON_DATA_DIR
        self._sra_data_dir = utils.SRA_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

        study_id = 'BII-S-7'
        self._inv_obj = isajson.load(open(os.path.join(self._json_data_dir, study_id, study_id + '.json')))
        self._study_sra_data_dir = os.path.join(self._sra_data_dir, study_id)
        self._expected_submission_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'submission.xml'), 'rb').read())
        self._expected_project_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'project_set.xml'),
                                                                 'rb').read())
        self._expected_sample_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'sample_set.xml'),
                                                                 'rb').read())
        self._expected_exp_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'experiment_set.xml'),
                                                                  'rb').read())
        self._expected_run_set_xml_obj = etree.fromstring(open(os.path.join(self._study_sra_data_dir, 'run_set.xml'),
                                                               'rb').read())

        self._sra_default_config = {
            "sra_broker": "",
            "sra_center": "OXFORD",
            "sra_project": "OXFORD",
            "sra_lab": "Oxford e-Research Centre",
            "sra_broker_inform_on_status": "proccaserra@gmail.com",
            "sra_broker_inform_on_error": "proccaserra@gmail.com",
            "sra_broker_contact_name": "PRS"
        }

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_sra_export_submission_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_submission_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'submission.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_submission_xml_obj, actual_submission_xml_obj))

    def test_sra_export_sample_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_sample_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'sample_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_sample_set_xml_obj, actual_sample_set_xml_obj))

    def test_sra_export_experiment_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_exp_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'experiment_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_exp_set_xml_obj, actual_exp_set_xml_obj))

    def test_sra_export_run_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_run_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'run_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_run_set_xml_obj, actual_run_set_xml_obj))

    def test_sra_export_project_set_xml(self):
        sra.export(self._inv_obj, self._tmp_dir, sra_settings=self._sra_default_config)
        actual_project_set_xml_obj = etree.fromstring(open(os.path.join(self._tmp_dir, 'project_set.xml'), 'rb').read())
        self.assertTrue(utils.assert_xml_equal(self._expected_project_set_xml_obj, actual_project_set_xml_obj))

    def test_create_datafile_hashes_success(self):
        datafilehashes = sra.create_datafile_hashes(os.path.join(utils.TAB_DATA_DIR, 'BII-S-7'), ['1EU.sff'])
        self.assertEqual(datafilehashes['1EU.sff'], 'd41d8cd98f00b204e9800998ecf8427e')  # hash is for empty file

    def test_create_datafile_hashes_fail(self):
        with self.assertRaises(FileNotFoundError):
            sra.create_datafile_hashes(os.path.join(utils.TAB_DATA_DIR, 'BII-S-7'), ['1EU'])

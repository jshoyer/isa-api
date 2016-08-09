import unittest
import os
import shutil
from isatools.convert import isatab2sra
from tests import utils
import tempfile


class TestIsaTab2Sra(unittest.TestCase):

    def setUp(self):
        self._tab_data_dir = utils.TAB_DATA_DIR
        self._sra_config_dir = utils.DEFAULT2015_XML_CONFIGS_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_isatab2sra_dump_dir_exists_chromatin_mod_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-chromatin-mod-seq'), self._tmp_dir,
                              self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_env_gene_survey(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-env-gene-survey-seq'), self._tmp_dir,
                              self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_exome_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-exome-seq'), self._tmp_dir,
                              self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_genome_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-genome-seq'), self._tmp_dir,
                              self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_protein_dna_interaction_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-protein-dna-interaction-seq'),
                              self._tmp_dir, self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_protein_rna_interaction_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-protein-rna-interaction-seq'),
                              self._tmp_dir, self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))

    def test_isatab2sra_dump_dir_exists_transcriptome_seq(self):
        isatab2sra.create_sra(os.path.join(self._tab_data_dir, 'TEST-ISA-SRA-transcriptome-seq'), self._tmp_dir,
                              self._sra_config_dir)
        self.assertTrue(os.path.exists(os.path.join(self._tmp_dir, 'sra')))
import os
import shutil
import unittest
import monkey.monkey.cell.cell_helper as cell_helper 

class TestStatic():
    
    def setup(self):
        self.sample_corpus = corpus.Corpus("test_static", 2)
        self.sample_cell_helper = cell_helpter.CellHelper("monkey/test_static", 5)
       
    def teardown(self):
        try:
            shutil.rmtree("monkey/test_static")
        except Exception:
            pass
    
    def test_cell_helper(self):
        test_corpus.get_next_images()
        self.sample_cell_helper.imprint()
        assert not self.sample_cell_helper.getPrototype() is None


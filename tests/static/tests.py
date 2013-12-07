import os
import shutil
import monkey.corpus as corpus
import monkey.helpers.cell_helper as cell_helper 
import monkey.helpers.static_helper as static_helper

class TestStatic():
    
    def setup(self):
        path = "monkey/test_static"
        self.sample_corpus = corpus.Corpus(path, 2)
        self.sample_cell_helper = cell_helper.CellHelper(path, 5)
        selt.sample_static_helper = static_helper.StaticHelper(path, None, 5, sample_corpus)
       
    def teardown(self):
        try:
            shutil.rmtree("monkey/test_static")
        except Exception:
            pass
    
    def test_cell_helper(self):
        self.sample_corpus.get_next_images()
        assert not self.sample_cell_helper.imprint() is None

    def test_static_helper(self):
        assert not self.static_helper.imprint() is None
        

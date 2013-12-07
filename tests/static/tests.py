import os
import shutil
import monkey.monkey.corpus.corpus as corpus
import monkey.monkey.cell.cell_helper as cell_helper 

class TestStatic():
    
    def setup(self):
        self.sample_corpus = corpus.Corpus("monkey/test_static", 2)
        self.sample_cell_helper = cell_helper.CellHelper("monkey/test_static", 5)
       
    def teardown(self):
        try:
            shutil.rmtree("monkey/test_static")
        except Exception:
            pass
    
    def test_cell_helper(self):
        self.sample_corpus.get_next_images()
        self.sample_cell_helper.imprint()
        assert not self.sample_cell_helper.getPrototype() is None

    def test_static_helper(self):
        

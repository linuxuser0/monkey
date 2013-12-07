import os
import shutil
import unittest
import monkey.monkey.corpus.corpus as corpus

class TestCorpus():
    
    def setup(self):
        try:
            shutil.rmtree("monkey/test")
        except Exception:
            pass

        self.test_corpus = corpus.Corpus("test", 2)
        
    def teardown(self):
        try:
            shutil.rmtree("monkey/test")
        except Exception:
            pass

    def test_corpus_init(self):
        assert os.path.isdir("monkey/test")
        assert len(os.listdir("monkey/test/data/targets")) > 0
        assert len(os.listdir("monkey/test/data/distractors")) > 0

    def test_corpus_next_images(self):
        assert len(os.listdir("monkey/test/cell")) == 0
        self.test_corpus.get_next_images()
        after_targets = after_distractors = None
        try:
            after_targets = len(os.listdir("monkey/test/cell/targets"))
        except Exception:
            pass
        try:
            after_distractors = len(os.listdir("monkey/test/cell/distractors"))
        except Exception:
            pass
        assert after_distractors > 0 or after_targets > 0 
        

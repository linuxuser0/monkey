import unittest
import monkey.corpus as corpus

class TestMonkey(unittest.TestCase):

    def setUp(self):
        self.corpus = corpus.Corpus()

    def test_corpus_init(self):
        self.corpus 

    def test_corpus_next_image(self):
        pass

if __name__ == '__main__':
    unittest.main()

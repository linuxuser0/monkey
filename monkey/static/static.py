from glimpse.glab.api import *
import monkey.corpus.corpus as corpus

class Static():

    def __init__(self, percent):
         self.c = corpus.Corpus("static", percent)
         SetCorpus(self.c.get_corpus())
         print("Corpus initialized") 

    def run(self, times, interval):
        for x in xrange(times): 
            self.step()
            print("Step " + str(x) + " complete")
            if x % interval == 0:
                self.classify()
                print("Classification complete")

        print("Results below.")
            
    def step(self):
        ImprintS2Prototypes(10)
        self.c.get_next_image()

    def classify(self):
        print(EvaluateClassifier())


from glimpse.glab.api import *
import monkey.corpus.corpus as corpus

class Static():

    def __init__(self, initial, add, percent):
         self.c = corpus.Corpus("static", percent)
         self.initial = initial
         self.add = add
         self.percent = percent
         SetCorpus(self.c.get_corpus())
         ImprintS2Prototypes(initial)
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
        self.c.get_next_image()
        SetS2Prototypes(GetPrototype() + StaticHelper(self.add).getPrototype())

    def classify(self):
        print(EvaluateClassifier())


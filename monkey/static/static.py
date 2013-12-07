from glimpse.glab.api import *
import monkey.corpus.corpus as corpus
import static_helper

class Static():

    def __init__(self, initial, add, percent):
         self.c = corpus.Corpus("static", percent)
         self.initial = initial
         self.add = add
         self.percent = percent
         self.results = []
         SetCorpus(self.c.get_corpus())
         ImprintS2Prototypes(initial)
         self.prototype = GetPrototype()
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
        self.c.get_next_images()
        StoreExperiment("experiments")
        self.prototype, test_results = static_helper.StaticHelper().imprint_new_cells(self.prototype, self.add, self.c.get_corpus())
        LoadExperiment("experiments")
        self.results.append(test_results)

    def classify(self):
        print(EvaluateClassifier())


import glimpse.experiment
import glimpse.models
import monkey.corpus
import monkey.helpers.static_helper

class Static():

    def __init__(self, window=None, delta=2, percent=50): 
         self.corpus = monkey.corpus.Corpus("static", percent)
         self.window = window 
         self.delta = delta
         self.percent = percent
         self.results = []
         self.exp = glimpse.experiment.ExperimentData()
         glimpse.experiment.SetModel(self.exp, model=glimpse.models.MakeModel())
         glimpse.experiment.SetCorpus(self.exp, self.corpus.get_corpus())
         glimpse.experiment.MakePrototypes(self.exp, num_prototypes=window, algorithm="imprint")
         self.prototypes = [[glimpse.experiment.GetPrototype(self.exp, n)] for n in range(
             glimpse.experiment.GetNumPrototypes(self.exp))]

    def run(self, times):
        for x in xrange(times): 
            self.step()
            
    def step(self):
        self.corpus.get_next_images()
        self.prototype, test_results = monkey.helpers.static_helper.StaticHelper(
                "static", self.prototypes, self.delta, self.window).imprint()
        self.results.append(test_results)



import glimpse.experiment
import glimpse.models
import monkey.corpus
import monkey.helpers.static_helper

class Static():

    def __init__(self, initial, add, percent):
         self.corpus = monkey.corpus.Corpus("static", percent)
         self.initial = initial
         self.add = add
         self.percent = percent
         self.results = []
         self.exp = glimpse.experiment.ExperimentData()
         glimpse.experiment.SetModel(self.exp, model=glimpse.models.MakeModel())
         glimpse.experiment.SetCorpus(self.exp, self.corpus.get_corpus())
         glimpse.experiment.MakePrototypes(self.exp, num_prototypes=10, algorithm="imprint")
         self.prototypes = [glimpse.experiment.GetPrototype(self.exp, n) for n in range(
             glimpse.experiment.GetNumPrototypes(self.exp))]

    def run(self, times, interval):
        for x in xrange(times): 
            self.step()
            
    def step(self):
        self.c.get_next_images()
        self.prototype, test_results = static_helper.StaticHelper("static", self.prototypes, self.add).imprint()
        self.results.append(test_results)



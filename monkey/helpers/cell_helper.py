import os
import glimpse.experiment
import glimpse.models

class CellHelper():
    
    def __init__(self, path, count): 
        self.path = path
        self.count = count
        self.exp = glimpse.experiment.ExperimentData()
        self.corpus = os.path.join(self.path, "cell")
        self.exp.extractor.model = glimpse.models.MakeModel()
        print self.corpus

    def imprint(self):
        glimpse.experiment.SetCorpus(self.exp, self.corpus) 
        glimpse.experiment.MakePrototypes(self.exp, num_prototypes=self.count, algorithm="imprint")
        return [glimpse.experiment.GetPrototype(self.exp, n) for n in range(
            glimpse.experiment.GetNumPrototypes(self.exp))]


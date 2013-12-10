import os
import glimpse.experiment

class CellHelper():
    
    def __init__(self, path, count): 
        self.path = path
        self.count = count
        self.exp = glimpse.experiment.ExperimentData()

    def imprint(self):
        glimpse.experiment.SetCorpus(os.path.join(self.path, "cell"))
        glimpse.experiment.MakePrototypes(self.exp, num_prototypes=self.count, algorithm="imprint")
        return [[glimpse.experiment.GetPrototype(self.exp, n)] for n in range(
            glimpse.experiment.GetNumPrototypes(self.exp))]


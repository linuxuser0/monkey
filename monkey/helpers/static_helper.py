import os
import numpy
import glimpse.experiment
import cell_helper

class StaticHelper():
    def __init__(self, path, prototype, add): #make corpus a STRING, not a CORPUS
        self.path = path
        self.prototypes = prototypes
        self.add = add
        self.exp = glimpse.experiment.ExperimentData()
        self.corpus = os.path.join(self.path, "data") 

    def imprint(self):
        helper = cell_helper.CellHelper(self.path, self.add)
        print "self.prototype:"
        print self.prototypes
        print "helper.imprint()"
        print helper.imprint()
        new_prototypes = numpy.concatenate([self.prototype, helper.imprint()])
        print "new_prototype"
        print new_prototypes
        print type(self.prototype)
        glimpse.experiment.SetCorpus(self.exp, self.corpus)
        self.exp.extractor.model.s2_prototypes = new_prototypes
        glimpse.experiment.EvaluateClassifier()
        results = glimpse.experiment.GetEvaluationResults().score
        return new_prototype, results 

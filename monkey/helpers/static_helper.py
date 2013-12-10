import os
import numpy
import glimpse.pools
import glimpse.models
import glimpse.experiment
import cell_helper

class StaticHelper():

    def __init__(self, path, prototypes, add, layer="C2"): 
        self.path = path
        self.prototypes = numpy.concatenate(prototypes)
        self.add = add
        self.exp = glimpse.experiment.ExperimentData()
        self.corpus = os.path.join(self.path, "data") 
        self.exp.extractor.model = glimpse.models.MakeModel()
        self.layer = layer
        self.pool = glimpse.pools.MakePool()

    def imprint(self):
        helper = cell_helper.CellHelper(self.path, self.add)
        helper_prototypes = numpy.concatenate([helper.imprint()])
        new_prototypes = numpy.concatenate([self.prototypes, helper_prototypes])
        
        glimpse.experiment.SetCorpus(self.exp, self.corpus)
        print self.exp.extractor.model.params.s2_kernel_shapes
        self.exp.extractor.model.s2_kernels = [new_prototypes]
        print "Computing activation:"
        glimpse.experiment.ComputeActivation(self.exp, self.layer, self.pool)
        print "Training and testing classifier:"
        glimpse.experiment.TrainAndTestClassifier(self.exp)
        results = glimpse.experiment.GetEvaluationResults().score
        print "RESULTS:"
        print results
        print "Mission success."
        exit()
        return new_prototype, results 

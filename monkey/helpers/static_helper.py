import os
import numpy
import glimpse.pools
import glimpse.models
import glimpse.experiment
import cell_helper

class StaticHelper():

    def __init__(self, path, prototypes, delta, window, layer="C2"): 
        self.path = path
        self.prototypes = numpy.concatenate(prototypes)
        self.delta = delta
        self.window = window
        self.exp = glimpse.experiment.ExperimentData()
        self.corpus = os.path.join(self.path, "data") 
        self.exp.extractor.model = glimpse.models.MakeModel()
        self.layer = layer
        self.pool = glimpse.pools.MakePool()
        self.results = []
        self.helper = cell_helper.CellHelper(self.path, self.delta)

    def imprint(self):

        helper_prototypes = numpy.concatenate([self.helper.imprint()])
        if self.window is not None: 
            self.prototypes = self.prototypes[self.delta:] 

        new_prototypes = numpy.concatenate([self.prototypes, helper_prototypes])
        print "NEWPROTOSHAPE"
        print new_prototypes.shape
        
        glimpse.experiment.SetCorpus(self.exp, self.corpus)
        print self.exp.extractor.model.params.s2_kernel_shapes
        self.exp.extractor.model.s2_kernels = [new_prototypes]
        print "Computing activation:"
        glimpse.experiment.ComputeActivation(self.exp, self.layer, self.pool)
        print "Training and testing classifier:"
        glimpse.experiment.TrainAndTestClassifier(self.exp, self.layer)
        results = glimpse.experiment.GetEvaluationResults(self.exp).score
        print "RESULTS:"
        print results 
        self.prototypes = new_prototypes 
        self.results.append(results)

    def step(self):
        self.helper.get_next_images()
        self.imprint()
        

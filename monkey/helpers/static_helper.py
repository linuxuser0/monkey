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
        print self.prototypes.shape
        #print helper.imprint().shape
        #print "self.prototype:"
        #print self.prototypes
        #print "helper.imprint()"
        #print helper.imprint()
        new_prototypes = [numpy.concatenate([self.prototypes, helper.imprint()])]
       # print "new_prototype"
       # print new_prototypes
        
        glimpse.experiment.SetCorpus(self.exp, self.corpus)
        print self.exp.extractor.model.params.s2_kernel_shapes
        self.exp.extractor.model.s2_kernels = new_prototypes
        glimpse.experiment.ComputeActivation(self.exp, self.layer, self.pool)
        glimpse.experiment.TrainAndTestClassifier(self.exp)
        results = glimpse.experiment.GetEvaluationResults().score
        print "RESULTS:"

        print results
        return new_prototype, results 

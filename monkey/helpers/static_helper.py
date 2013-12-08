import os
import numpy
from glimpse.glab.api import *
import cell_helper

class StaticHelper():
    def __init__(self, path, prototype, add): #make corpus a STRING, not a CORPUS
        self.path = path
        self.prototype = prototype
        self.add = add
        self.corpus = os.path.join(self.path, "data") 

    def imprint(self):
        helper = cell_helper.CellHelper(self.path, self.add)
        print "self.prototype:"
        print self.prototype
        print "helper.imprint()"
        print helper.imprint()
        new_prototype = numpy.concatenate([self.prototype, helper.imprint()])
        print "new_prototype"
        print new_prototype
        print type(self.prototype)
        Reset()
        SetCorpus(self.corpus)
        SetS2Prototypes(self.prototype)
        EvaluateClassifier()
        results = GetEvaluationResults().score
        return new_prototype, results 

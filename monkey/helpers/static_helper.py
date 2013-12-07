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
        prototype = numpy.append(self.prototype, helper.imprint())
        Reset()
        print self.corpus
        SetCorpus(self.corpus)
        SetS2Prototypes(self.prototype)
        EvaluateClassifier()
        results = GetEvaluationResults().score
        return prototype, results 

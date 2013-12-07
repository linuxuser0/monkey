import numpy
from glimpse.glab.api import *
import cell_helper

class StaticHelper():
    def __init__(self):
        pass

    def imprint_new_cells(self, prototype, add, corpus):
        prototype = numpy.concatentate(prototype, cell_helper.CellHelper(add).getPrototype())
        Reset()
        SetCorpus(corpus)
        SetS2Prototypes(prototype) #not setting properly - DEBUG!
        EvaluateClassifier()
        results = GetEvaluationResults().score
        return prototype, results 

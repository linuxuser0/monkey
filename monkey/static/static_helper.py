from glimpse.glab.api import *
import cell_helper

class StaticHelper():
    def __init__(self):
        pass

    def imprint_new_cells(self, prototype, add, corpus):
        cells = cell_helper.CellHelper(add).getPrototype()
        Reset()
        SetCorpus(corpus)
        SetS2Prototypes(prototype + cells)

        finalproto = GetPrototype()
        results = GetEvaluationResults().score
        return finalproto, results 

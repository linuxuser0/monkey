from glimpse.glap.api import *

class StaticHelper():
    def __init__():
        pass

    def imprint_new_cells(prototype):
        cells = cell_helper.CellHelper().getPrototype()
        SetS2Prototypes(prototype + cells)
        finalproto = GetPrototype()
        results = GetEvaluationResults().score
        return finalproto, results 

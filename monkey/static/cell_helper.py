import os
from glimpse.glab.api import *

class CellHelper():
    
    def __init__(self, count): #add path
        Reset()
        self.cd = os.path.dirname(os.path.realpath(__file__))
        SetCorpus(os.path.join(self.cd, "cell"))
        ImprintS2Prototypes(count)

    def getPrototype(self):
        return GetPrototype()

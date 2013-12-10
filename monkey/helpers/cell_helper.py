import os
from glimpse.glab.api import *

class CellHelper():
    
    def __init__(self, path, count): #add path
        self.path = path
        self.count = count

    def imprint(self):
        Reset()
        SetCorpus(os.path.join(self.path, "cell"))
        print "CELL PROTOTYPES", self.count
        ImprintS2Prototypes(self.count)
        print "CELL PROTOTYPE"
        print GetPrototype()
        return GetPrototype()


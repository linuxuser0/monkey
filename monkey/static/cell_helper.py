from glimpse.glab.api import *

class CellHelper():
    
    def __init__(self, count):
        print("SETTING CORPUS - SHOULD ONLY DO ONCE")
        SetCorpus("cell") #ISSUE! Being set by called class - how to do multiple glimpse instances?
        ImprintS2Prototypes(count)

    def getPrototype():
        return GetPrototype()

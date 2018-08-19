# Document Name: ExampleHub.py
# Author: Jesse Campbell
# Date Created: August 19 2018

from simlib.hub import Hub

class ExampleHub(Hub):
    def __init__(self):
        super().__init__()
        self.algorithm = self.superSmartTrilaterationAlgorithm

    def superSmartTrilaterationAlgorithm(self, mapDict : dict, nodeEntry : int, anchorCount : int) -> list:
        ''' placeholder'''
        return [mapDict[0, nodeEntry], mapDict[1, nodeEntry], mapDict[2, nodeEntry]]

    def mainloop(self):
        pass

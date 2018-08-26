#!/usr/bin/env python3
# Document Name: ExampleHub.py
# Author: Jesse Campbell
# Date Created: August 19 2018

from hub import Hub
import sys

class ExampleHub(Hub):
    def __init__(self):
        super().__init__()
        self.algorithm = self.superSmartTrilaterationAlgorithm

    def superSmartTrilaterationAlgorithm(self, mapDict : dict, nodeEntry : int, anchorCount : int) -> list:
        ''' placeholder'''
        return [mapDict[0, nodeEntry], mapDict[1, nodeEntry], mapDict[2, nodeEntry]]

    def mainloop(self):
        pass

if __name__ == "__main__" :
    # TODO
    sys.exit( 0 )

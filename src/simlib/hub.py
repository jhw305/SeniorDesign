# Document Name: Hub.py
# Author: Jesse Campbell
# Date Created: August 18 2018

from simulated import Simulated
from anchor import Anchor
from node import Node

class Hub(Simulated):
    def __init__(self, algorithm):
        #super().__init__()
        self.time = 0
        self.anchors = list()
        self.nodes = list()
        #'map' is a dictionary of tuples to store distance data from each anchor to each node
        self.map = {}
        self.nodePositions = {}
        #A function pointer that gets called in Hub.triliterate
        self.algorithm = algorithm

    def setTime(time : int):
        self.time = time

    def containsAnchor(self, anchor : "Anchor") -> bool:
        ''' Checks to see if the argument exists in Hub.anchors '''
        if (anchor in self.anchors):
            return True
        return False

    def addAnchor(self, anchor : "Anchor"):
        ''' Adds an Anchor to Hub.anchors. Resets the map '''
        try:
            assert(isinstance(anchor, Anchor))
        except:
            print("Hub.addAnchor: Non-anchor object cannot be added to Hub.anchors")
            raise

        if (anchor in self.anchors):
            print(f'Hub.addAnchor: Anchor {anchor.ID} is already a member of Hub.anchors')
        else:
            self.anchors.append(anchor)
            self.resetMap()

    def removeAnchor(self, anchor : "Anchor"):
        ''' Removes an Anchor from Hub.anchors. Resets the map '''
        try:
            assert(isinstance(anchor, Anchor))
        except:
            print("Hub.removeAnchor: Non-anchor object cannot be removed from Hub.anchors")
            raise
        
        if (anchor in self.anchors):
            self.anchors.remove(anchor)
            self.resetMap()
        else:
            print(f'Hub.removeAnchor: Anchor {anchor.ID} is not a member of Hub.anchors')

    def containsNode(self, node : "Node") -> bool:
        ''' Checks to see if the argument exists in Hub.nodes '''
        if (node in self.nodes):
            return True
        return False

    def addNode(self, node : "Node"):
        ''' Adds a Node to Hub.nodes. Resets the map '''
        try:
            assert(isinstance(node, Node))
        except:
            print("Hub.addAnchor: Non-node object cannot be added to Hub.nodes")
            raise
        
        if (node in self.nodes):
            print(f'Hub.addNode: Node {node.ID} is already a member of Hub.nodes')
        else:
            self.nodes.append(node)
            self.resetMap()

    def removeNode(self, node : "Node"):
        ''' Removes a Node from Hub.nodes. Resets the map '''
        try:
            assert(isinstance(node, Node))
        except:
            print("Hub.addAnchor: Non-node object cannot be removed from Hub.nodes")
            raise
        
        if (node in self.nodes):
            self.nodes.remove(node)
            self.resetMap()
        else:
            print(f'Hub.removeNode: Node {node.ID} is not a member of Hub.nodes')

    def resetMap(self):
        ''' Resets the map to [][] '''
        self.map = {}

    def mapDistance(self, xVal : int, yVal : int, distance : int):
        ''' Adds the measured distance to the anchor/node pair '''
        self.map[x, y] = distance

    def getNodePosition(self, node : "Node"):
        '''
        Each anchor in Hub.anchors will have requestPing called.
        Once a response is gathered from each anchor, Hub.triliterate is called
        '''
        try:
            assert(isinstance(node, Node))
        except:
            print("Hub.getNodePosition: Non-node object cannot be pinged by anchors in Hub.anchors")
            raise
        
        for anchor in self.anchors:
            anchor.requestPing(node)
            self.addAction(self.mapAnchorToNode, [anchor, node])
        self.addAction(self.triliterate, [])

    def mapAnchorAndNode(self, *args : "Anchor, Node"):
        '''
        Always called after an requestPing is called by an anchor. Adds itself to the top of the actionQueue
        if the given anchor has not received a response yet.
        '''
        try:
            assert(len(args) == 2)
        except:
            print('Hub.mapAnchorAndNode: Invalid number of arguments')
            raise
        
        anchor = args[0]
        node = args[1]
        
        try:
            assert(isinstance(anchor, Anchor))
        except:
            print("Hub.mapAnchorAndNode: Non-Anchor object passed as first parameter")
            raise
        
        try:
            assert(isinstance(node, Node))
        except:
            print("Hub.mapAnchorAndNode: Non-node object passed as second parameter")
            raise

        if (anchor.pingedNodeID == node.ID and anchor.measurement > 0):
            ''' Adds the measured distance to Hub.map '''
            #Finds position of anchor in Hub.anchors
            x = self.anchors.index(anchor)
            y = self.nodes.index(node)
            mapDistance(x, y, anchor.measurement)
        else:
            ''' Puts itself back infront of the action queue '''
            self.prependAction(self.mapAnchorToNode, [anchor, node])
        
    def triliterateNode(node : "Node"):
        '''
        Calls the triliteration alogrithm passed to the Constructor, passing a dictionary of tuples and intergers
        '''
        position = self.algorithm(self.map, self.nodes.index(node))
        self.nodePosition[node.getID()] = position

    def generateCompleteMap(self):
        '''
        Generates a complete map of anchors and nodes
        '''
        for node in nodes:
            self.getNodePosition(node)

    def addAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueue.addAction(function, args, ctr)

    def prependAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueue.prependAction(function, args, ctr)


    def mainloop():
        pass
    '''
        Left blank because:
            Its unclear how to write this that isn't specific to an algorithm
            Unclear what the arguments are supposed to be for super().mainloop
    '''


if __name__=='__main__':
    #unit tests?
    hub = Hub(0)
    hub.addAnchor(0)

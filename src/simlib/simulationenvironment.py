# Document Name: SimulationEnvironment.py
# Author: Jesse Campbell
# Date Created: August 18 2018
'''
Things to consider:
   1 Actions with potentially no time requirement can be added to the action queue, and they should all be executed in the same
        update() call
   2 Some actions require waiting for some flags to be set or values to be updated on other devices, so there needs to be a way
        for actions to not be deleted from the actionQueue even if the counter is at 0.
   3 On that note, some functions in the action queue want to be called until they return a certain value. How do we go about
        keeping those actions in the actionqueue? Do we just add the same action to the queue if the check fails? If so, how
        do we rectify the above problem (2)?

'''

from archspec import ArchSpec
from hub import Hub
from anchor import Anchor
from node import Node

class SimulationEnvironment():
    def __init__(self):
        self.time = 0
        self.hubs = list()
        self.anchors = list()
        self.nodes = list()
        self.nextID = 0
        self.signalList = []

    def createHub(self, algorithm : "function") -> "Hub":
        ''' Creates a hub, adds it to simEnv list of hubs, returns hub '''
        hub = Hub(algorithm)
        self.hubs.append(Hub)
        return hub

    def createNode(self, xPos : int, yPos : int, zPos: int,
                   xVel : int, yVel : int, zVel: int) -> "Node":
        ''' Creates a node, adds it to simEnv list of nodes, returns node '''
        node = Node(self.nextID, xPos, yPos, zPos, xVel, yVel, zVel, self.signalList)
        self.nextID += 1
        self.nodes.append(node)
        return node

    def getNodeByID(self, ID : int) -> "Node":
        ''' Scans the simEnv's list of nodes and returns one with a matching ID '''
        for node in nodes:
            if (ID == node.ID):
                return node

    def associateNode(self, hub : "Hub", node : "Node"):
        ''' Adds the node to the Hub's list of nodes '''
        hub.addNode(node)

    def dissassociateNode(self, hub : "Hub", node : "Node"):
        ''' Removes the node from the Hub's list of nodes '''
        hub.removeNode(node)

    def deleteNode(self, node : "Node"):
        ''' Deletes the node, and dissassociates it from each relevant hubs '''
        for hub in hubs:
            if (hub.containsNode(node)):
                dissassociateNode(hub, node)
        self.nodes.remove(node)

    def createAnchor(self, xPos : int, yPos : int, zPos: int) -> "Anchor":
        ''' Creates an anchor, adds it to simEnv list of anchors, returns anchor '''
        anchor = Anchor(self.nextID, xPos, yPos, zPos, self.signalList)
        self.nextID += 1
        self.anchors.append(anchor)
        return anchor

    def getAnchorByID(self, ID : int) -> "Anchor":
        ''' Scans the simEnv's list of anchors and returns one with a matching ID '''
        for anchor in anchors:
            if (ID == anchor.ID):
                return anchor

    def associateAnchor(self, hub : "Hub", anchor : "Anchor"):
        ''' Adds the anchor to the Hub's list of anchors '''
        hub.addAnchor(anchor)

    def dissassociateAnchor(hub : "Hub", anchor : "Anchor"):
        ''' Removes the anchor from the Hub's list of anchors '''
        hub.removeAnchor(anchor)

    def deleteAnchor(self, anchor : "Anchor"):
        ''' Deletes the anchor, and dissassociates it from each relevant hubs '''
        for hub in hubs:
            if (hub.containsAnchor(anchor)):
                dissasociateAnchor(hub, anchor)
        self.anchors.remove(anchor)

    def mainloop():
        pass
    
def superSmartTrilaterationAlgorithm(mapDict : dict, nodeEntry : int) -> list:
    return [0, 0, 0]

if __name__ == '__main__':
    # Unit Test
    errors = 0

    archspec = ArchSpec(Hub, Anchor, Node)
    simEnv = SimulationEnvironment()
    hub = simEnv.createHub(superSmartTrilaterationAlgorithm)
    for i in range(0,4):
        anchor = simEnv.createAnchor(0, 0, i)
        simEnv.associateAnchor(hub, anchor)
    node = simEnv.createNode(3, 3, 3, 0, 0, 0)
    hub.getNodePosition(node)
    while(1):
        simEnv.mainloop()
        
    

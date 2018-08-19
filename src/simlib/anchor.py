# Document Name: Anchor.py
# Author: Jesse Campbell
# Date Created: August 18 2018

from simulated import Simulated
from FSM import Device, AVAILABLE_STATES, INITIAL_STATE, DEVICE_DATA
from node import Node

class Anchor(Device):
    def __init__(self, ID : int, xPos : int, yPos : int, zPos : int,
                 signalList: list):
        super().__init__(AVAILABLE_STATES, INITIAL_STATE, DEVICE_DATA)
        self.time = 0
        self.ID = ID
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.pingedNodeID = 0
        self.measurement = 0
        # signal list format -> [ [ fromID, destinationID ] ]
        self.signalList = signalList

    def setTime(time : int):
        self.time = time

    def getID() -> int:
        return self.ID

    def listenForSignal() -> int:
        '''
        Searches to see if it is the target of any signals. Returns the sending ID
        if a signal is found or 0 if no signal is found.
        '''
        for signal in signalList:
            if (self.ID == signal[1]):
                return signal[0]
        return 0

    def requestPing(self, node : "Node"):
        '''
        Adds a pingNode function call to the action queue
        '''
        try:
            assert(isinstance(node, Node))
        except:
            print("Anchor.requestPing: Non-node object cannot be pinged by anchors in Hub.anchors")
            raise
        
        self.addAction(self.pingNode, [node])

    def pingNode(self, *args : "Node"):
        '''
        Sends out a signal to a node, and waits for a reply
        '''
        node = args[0]
        nodeID = node.getID()
        self.pingedNodeID = nodeID
        signalList.append([self.ID, nodeID])
        self.addAction(self.waitForReply, [node])

    def waitForReply(self, *args : "Node"):
        '''
        Waits for a reply by the node. Adds itself to the top of the actionQueue
        if the given node has not replied
        '''
        node = args[0]
        nodeID = node.getID()
        ResponderID = listenForSignal()
        if (ResponderID == nodeID):
            dis = ManufactureError(self.xPos, self.yPos, self.zPos,
                                        node.xPos, node.yPos, node.zPos)
            self.distance = dis
        else:
            self.prependAction(self.waitForReply, node)

    def addAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueue.addAction(function, args, ctr)

    def prependAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueue.prependAction(function, args, ctr)
            
'''
    def mainloop():
        pass
'''

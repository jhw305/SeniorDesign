# Document Name: Node.py
# Author: Jesse Campbell
# Date Created: August 18 2018

from simlib.simulated import Simulated
from simlib.FSM import Device
from abc import ABC

class Node(Device):
    def __init__(self, ID : int, xPos : int, yPos : int, zPos : int,
                                 xVel : int, yVel : int, zVel : int,
                 signalList : list):
        #super().__init__()
        self.time = 0
        self.ID = ID
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.xVel = xVel
        self.yVel = yVel
        self.zVel = zVel
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

    def addAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueue.addToQueue(function, args, ctr)

    def prependAction(self, function : "Function", args : list, ctr : int = 0):
        self.actionQueueprependAction(function, args, ctr)
    
'''
    def mainloop():
        pass
'''

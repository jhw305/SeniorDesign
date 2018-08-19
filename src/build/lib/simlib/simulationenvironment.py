#No device class, code does not run
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

from simulated import Simulated

class SimulationEnvironment():
    def __init__(self, mapPeriod : int, anchorCount : int, anchorDataList : list):
        self.time = 0
        self.hub = Hub(self, mapPeriod, self.time, anchorCount, anchorDataList)
        self.devices = self.hub.getAnchors()
        self.nextID = len(self.devices)
        self.signalList = []

    def update():
        #Calls the update function of each device and the hub, increments time
        self.time += 1
        nodeMap = self.hub.update(self.time)
        if (nodeMap):
            analyze(nodeMap)
        for device in devices:
            device.update(self.time)

    def addNode(self, coordinateList : list):
        #Calls the Device class constructor!!!!!!!!!!!!!!!
        newDevice = Device(self, self.time, self.nextID, coordinateList)
        self.devices.append(newDevice)
        self.hub.addNode(newDevice)

    def analyze(self, nodeMap : list):
        #Statistics I do not know how to do
        print(nodeMap)

    def sendSignalID(senderID : int, receiverID : int):
        self.signalList.append((receiverID, senderID))

    def checkAndDeleteSignal(receiverID: int, senderID : int):
        if ((receiverID, senderID) in self.signalList):
            self.signalList.remove((receiverID, senderID))
            self.signalList.remove((senderID, receiverID))
            return True
        else:
            return False
        

class Hub(Simulated):
    def __init__(self, simEnv, mapPeriod: int, time : int, anchorCount : int, anchorDataList : list):
        super()
        self.simEnv = simEnv
        self.time = time
        self.anchors = self.createAnchors(anchorCount, anchorDataList)
        self.nodes = []
        self.mapPeriod = mapPeriod #How much time inbetween mappings, starting at mapPeriod defined here
        self.nodeMap = []

    def update(time : int):
        self.time = time
        #Temporary functionality; Waits until time MAPPING_INTERVAL
        #and then generates a new map every time MAPPING_INTERVAL time has passed
        if (self.mapPeriod % self.time == 0 and self.time >= self.mapPeriod):
            super().addAction(createNodeMap, [])
            
        super.update()
        
    def getAnchors(self):
        return self.anchors

    def getSimEnv(self):
        return self.simEnv
    def addNode(self, node):
        self.nodes.append(node)
    
    def createAnchors(self, anchorCount : int, anchorDataList : list):
        for ID in range(0, anchorCount):
            #Calls the Device class constructor!!!!!!!!!!!!!!!
            anchorList = []
            anchorList.append(Device(self.simEnv, self.time, ID, anchorDataList[0]))
        return anchorList
            
    def createNodeMap():
        for node in self.nodes:
            super().addAction(pingNode, [node])
        super().addAction(triliterate, [])
        

    def pingNode(node):
        for anchor in self.anchors:
            anchor.pingNode(node)

    def triliterate():
        pass
            
'''
class Device(Simulated):
    def __init__(self, simEnv, time : int, ID : int, coordinates : list):
        super()
        self.simEnv = simEnv
        self.time = time
        self.ID = ID
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    def getID():
        return self.ID

    def pingNode(node): #Anchor oeratorion
        super().addAction(sendSignalID, [node.getID()])
        super().addAction(waitForResponse, [node.getID()])

    def sendSignalID(ID : int):
        self.simEnv.sendSignalID(self.ID, ID)

    #Temporary functionality
    def waitForResponse(ID : int):
        if (not self.simEnv.checkAndDeleteSignal(self.ID, ID)):
            super().addAction(waitForResponse, [node.getID()])

'''        

                          

if __name__ == '__main__':
    simEnv = SimulationEnvironment(mapPeriod = 500, anchorCount = 4, anchorDataList = [[0,0,0],
                                                                                       [0,0,10],
                                                                                       [0,10,0],
                                                                                       [10,0,0]])
    simEnv.addNode([3, 40, 19])
    simEnv.addNode([4, 40, 22])
    simEnv.addNode([3, 37, 4])
    

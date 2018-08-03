# Time is measure in microseconds and current is measured in milliamps
# each device should be run on its own thread so it can concurently 
# update its power useage and state of device.


#########################################################
# Sending constants from page 32 fig. 32 from datasheet #
#########################################################

OSC_STARTUP_SEND_CURRENT = 3
OSC_STARTUP_SEND_TIME = 2000

PLL_STARTUP_SEND_CURRENT = 12
PLL_STARTUP_SEND_TIME = 7

WR_TX_DATA_SEND_CURRENT = 15
WR_TX_DATA_SEND_TIME = 10

TX_SHR_SEND_CURRENT = 65
TX_SHR_SEND_TIME = 135 

TX_PHR_SEND_CURRENT = 48
TX_PHR_SEND_TIME = 1.33  #TIME PER BYTE OF INFO SENT


class State():
    def __init__(self, physical_data):
        self.physical_data = physical_data

    def getParam(self, param):
        return self.physical_data[param](self.physical_data)
        
        

class DeviceFSM():
    def __init__(self):
        self.state = "IDLE"
        self.ampmicrosecs = 0
        self.runtime = 0
    
    def idleState(self):
        pass

    def sendState(self, messagelen):
        self.state = "SEND"
        self.ampmicrosecs += OSC_STARTUP_SEND_CURRENT * OSC_STARTUP_SEND_TIME
        self.ampmicrosecs += PLL_STARTUP_SEND_CURRENT * PLL_STARTUP_SEND_TIME
        self.ampmicrosecs += WR_TX_DATA_SEND_CURRENT * WR_TX_DATA_SEND_TIME
        self.ampmicrosecs += TX_SHR_SEND_CURRENT * TX_SHR_SEND_TIME
        self.ampmicrosecs += TX_PHR_SEND_CURRENT * (TX_PHR_SEND_TIME * messagelen)  
        self.runtime += (OSC_STARTUP_SEND_TIME + PLL_STARTUP_SEND_TIME + WR_TX_DATA_SEND_TIME 
        + (TX_PHR_SEND_TIME*messagelen) + TX_SHR_SEND_TIME
        ) 
        self.state = "IDLE"

    def receiveStandardState(self):
        self.state = "RECEIVE"
        #do the same as sendstate from figure 33 page 32 of datasheet


    def receiveSniffState(self):
        self.state = "RECEIVE"
        #do similar to sendstate but now take into account 
        #the changes for sniff state i.e. per byte intermittent
        #lowering of current usage



    def getAmpMicrosecs(self):
        return self.ampmicrosecs

    def getState(self):
        return self.state

    def runFSM(self, timetorun, pingfreq, recievesniff):
        while timetorun > self.runtime:
            pass
            #Have a weighted rng to choose states based off of
            #how frequent we ping and then call the corresponding 
            #state to update with correct ampsmilisecs and runtime
            #for the device until we have run for the total timetorun
            #still needs to be written obviously
        

def getCurrent(physical_data):
    return 5

def getTime(physical_data):
    return 'time'

if __name__ == "__main__":
    data = {'current' : getCurrent, 'time' : getTime}
    s = State(data)
    
            






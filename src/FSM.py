# Time is measure in microseconds and current is measured in milliamps
# each device should be run on its own thread so it can concurently 
# update its power useage and state of device.


#########################################################
# Sending constants from page 32 fig. 32 from datasheet #
#########################################################

from simulated import Simulated
import simulated
from action import Action

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

DEBUG = True
 


class State():
    def __init__(self, physical_data):
        self.physical_data = physical_data

    def getParam(self, param):
        return self.physical_data[param](self.physical_data)


class Device(Simulated):
    def __init__(self, available_states, initial_state, physical_data):
        super(Device, self).__init__()
        self.available_states = available_states
        self.initial_state = initial_state
        self.dev_state = initial_state
        self.physical_data = physical_data
        self.next_states = []
        self.getAvailableNextStates()
        

    def setState(self, state):
        self.dev_state = state

    def getState(self):
        return self.dev_state

    def getAvailableNextStates(self):
        self.next_states =  self.available_states[self.dev_state]

    def setNextState(self, state):
        for next in self.next_states:
            if state in next:
                super().addAction(self.setState, [state])
                super().update()
                break

    def getParam(self, param):
        return self.physical_data[param](physical_data, self.dev_state.physical_data)
    
        

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

def getBattery(dev_data, state_data):
    battlife = battlife - state_data['current'](state_data)

STATE_1 = State({'current' : getCurrent, 'time' : getTime, 'state' : 1})
STATE_2 = State({'current' : getCurrent, 'time' : getTime, 'state' : 2})
STATE_3 = State({'current' : getCurrent, 'time' : getTime, 'state' : 3})
STATE_4 = State({'current' : getCurrent, 'time' : getTime, 'state' : 4})

INITIAL_STATE = STATE_1

DEVICE_DATA = {'batt_life' : getBattery}
AVAILABLE_STATES = {STATE_1 : [(STATE_2 , 4)] , STATE_2 : [(STATE_3 , 5) , (STATE_4 , 6)] , STATE_3 : [(STATE_3 , 1) , (STATE_4 , 8)] , STATE_4 : [(STATE_1 , 12)]}

if __name__ == "__main__":
    battlife = 1000
    device = Device(AVAILABLE_STATES, INITIAL_STATE, DEVICE_DATA)
    
    #checking state transitions to make sure they work
    print(device.next_states)
    device.setNextState(STATE_2)
    device.getAvailableNextStates()
    print(device.next_states)
    device.setNextState(STATE_3)
    device.getAvailableNextStates()
    print(device.next_states)
    device.setNextState(STATE_3)
    device.getAvailableNextStates()
    print(device.next_states)
    device.setNextState(STATE_1)
    device.getAvailableNextStates()
    print(device.next_states)

    #    
            






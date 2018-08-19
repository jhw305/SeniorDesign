# Document Name: DW1000_Anchor_1.py
# Author: Jesse Campbell
# Date Created: August 19 2018

from simlib.anchor import Anchor
from simlib.FSM import State

class DW1000_Anchor_1(Anchor):
    def __init__(self, nodeID : int, xPos : int, yPos : int, zPos : int, signalList : list):
        Anchor.__init__(self, nodeID, xPos, yPos, zPos, signalList)
        
        OFF_STATE = State({'current' : self.getOffCurrent, 'time' : self.getTime, 'state' : 'off_state'})
        DEEPSLEEP_STATE = State({'current' : self.getDeepSleepCurrent, 'time' : self.getTime, 'state' : 'deepsleep_state'})
        SLEEP_STATE = State({'current' : self.getSleepCurrent, 'time' : self.getTime, 'state' : 'sleep_state'})
        INIT_STATE = State({'current' : self.getInitCurrent, 'time' : self.getTime, 'state' : 'init_state'})
        IDLE_STATE = State({'current' : self.getIdleCurrent, 'time' : self.getTime, 'state' : 'idle_state'})
        RX_STATE = State({'current' : self.getRXCurrent, 'time' : self.getTime, 'state' : 'rx_state'})
        TX_STATE = State({'current' : self.getTXCurrent, 'time' : self.getTime, 'state' : 'tx_state'})
    
        INITIAL_STATE = OFF_STATE
        DEVICE_DATA = {'batt_life' : self.getBattery}
    
        AVAILABLE_STATES = {OFF_STATE : [(INIT_STATE, 3000)],
                            DEEPSLEEP_STATE : [(INIT_STATE, 3000)],
                            SLEEP_STATE : [(INIT_STATE, 3000)],
                            INIT_STATE : [(IDLE_STATE, 5)],
                            IDLE_STATE : [(RX_STATE, 0) , (TX_STATE, 0)],
                            RX_STATE : [(IDLE_STATE, 0) , (SLEEP_STATE, 0) , (DEEPSLEEP_STATE, 0)],
                            TX_STATE : [(IDLE_STATE, 0) , (SLEEP_STATE, 0) , (DEEPSLEEP_STATE, 0)]}

        self.available_states = AVAILABLE_STATES
        self.initial_state = INITIAL_STATE
        self.dev_state = INITIAL_STATE
        self.physical_data = DEVICE_DATA
        self.next_states = []
        self.getAvailableNextStates()

    def getOffCurrent(physical_data):
        return 0.0
    
    def getDeepSleepCurrent(physical_data):
        return 0.00005
    
    def getSleepCurrent(physical_data):
        return 0.001
    
    def getInitCurrent(physical_data):
        return 4.0
    
    def getIdleCurrent(physical_data):
        return 18.0
    
    def getRXCurrent(physical_data):
        return -10000.0
    
    def getTXCurrent(physical_data):
        return -10000.0
    
    def getTime(physical_data):
        return 'time'
    
    def getBattery(dev_data, state_data):
        battlife = battlife - state_data['current'](state_data)

    def mainloop(self):
        pass

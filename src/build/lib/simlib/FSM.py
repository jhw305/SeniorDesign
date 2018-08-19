#!/usr/bin/env python3

###################################################################################
# TIME WILL BE IN MICROSECONDS, CURRENT WILL BE IN MILLIAMPS                      #
###################################################################################
from simlib.simulated import Simulated
from abc import ABC , abstractmethod
from simlib.action import Action

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
    """
    Creates instance of a State for the device.
    """
    def __init__(self, physical_data : dict):
        self.physical_data = physical_data

    def getParam(self, param : str) -> 'unknown':
        """
        Calls a function based off of a physical
        parameter such as 'current' and returns the
        corrrect value for a given state.
        """
        return self.physical_data[param](self.physical_data)


class Device(Simulated , ABC):
    """
    Creates an instance of a device dependent on the FSM,
    physical data, and available states used to accurately
    model the DW1000 or other like devices. 
    """
    def __init__(self, available_states : dict, initial_state : State, physical_data : dict):
        Simulated.__init__(self)
        ABC.__init__(self)
        self.available_states = available_states
        self.initial_state = initial_state
        self.dev_state = initial_state
        self.physical_data = physical_data
        self.next_states = []
        self.__getAvailableNextStates()
        

    def __setState(self, state : State):
        """
        Sets the current state (dev_state) to the state provided.
        This is only called through setNextState.
        """
        self.dev_state = state
        self.__getAvailableNextStates( )

    def getState(self) -> State:
        """
        Returns the current state of the device. 
        """
        return self.dev_state

    def __getAvailableNextStates(self):
        """
        Gets the possible next states from the FSM
        and assigns them to the next_states.
        """
        self.next_states = self.available_states[self.dev_state]

    def setNextState(self, state : State):
        """
        Checks if the state provided is a valid next state
        and if so adds an action to the action queue to
        set the state.
        """
        for next in self.next_states:
            if state == next[ 0 ] :
                self.actionQueue.addToQueue( Action( self.__setState, [ state ] , next[ 1 ] ) )
                break

    def getParam(self, param : str) -> 'float' :
        """
        Gets a piece of physical data for the device such as
        battery life. 
        """
        return self.physical_data[param](physical_data, self.dev_state.physical_data)


if __name__ == "__main__":

    #####################################################################
    # This is dumb but i cant think of a way to do this while making it #
    # general to each device. I won't be adding comments to these       #
    # functions because they will be replaced when a better solution    #
    # is found.                                                         #
    #####################################################################
    
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
    
    ######################################################################################
    # FSM for the DW1000, includes states, thier delays, and the current for each state. # 
    ######################################################################################
        
    OFF_STATE = State({'current' : getOffCurrent, 'time' : getTime, 'state' : 'off_state'})
    DEEPSLEEP_STATE = State({'current' : getDeepSleepCurrent, 'time' : getTime, 'state' : 'deepsleep_state'})
    SLEEP_STATE = State({'current' : getSleepCurrent, 'time' : getTime, 'state' : 'sleep_state'})
    INIT_STATE = State({'current' : getInitCurrent, 'time' : getTime, 'state' : 'init_state'})
    IDLE_STATE = State({'current' : getIdleCurrent, 'time' : getTime, 'state' : 'idle_state'})
    RX_STATE = State({'current' : getRXCurrent, 'time' : getTime, 'state' : 'rx_state'})
    TX_STATE = State({'current' : getTXCurrent, 'time' : getTime, 'state' : 'tx_state'})
    
    INITIAL_STATE = OFF_STATE
    DEVICE_DATA = {'batt_life' : getBattery}
    
    AVAILABLE_STATES = {OFF_STATE : [(INIT_STATE, 3000)],
                        DEEPSLEEP_STATE : [(INIT_STATE, 3000)],
                        SLEEP_STATE : [(INIT_STATE, 3000)],
                        INIT_STATE : [(IDLE_STATE, 5)],
                        IDLE_STATE : [(RX_STATE, 0) , (TX_STATE, 0)],
                        RX_STATE : [(IDLE_STATE, 0) , (SLEEP_STATE, 0) , (DEEPSLEEP_STATE, 0)],
                        TX_STATE : [(IDLE_STATE, 0) , (SLEEP_STATE, 0) , (DEEPSLEEP_STATE, 0)]} 

    class DW1000( Device ) :
        def __init__(self, available_states : dict, initial_state : State, physical_data : dict) :
            Device.__init__( self , available_states , initial_state , physical_data )
        def mainloop( self, simlist: list ) :
                # TODO
                pass
                        
    battlife = 1000
    device = DW1000(AVAILABLE_STATES, INITIAL_STATE, DEVICE_DATA)
    
    #checking state transitions to make sure they work
    errors = 0
    simlist = [ ]
    my_current = device.getState().getParam('current')
    if my_current != 0.0 :
        print( "OFF_STATE current is incorrect! (Read: " + str( my_current ) + ")" )
        errors += 1
    device.setNextState(INIT_STATE)
    for i in range( 0 , 3000 ) :
	    device.run_timestep( simlist )
    my_current = device.getState().getParam('current')
    if my_current != 4.0 :
        print( "INIT_STATE current is incorrect! (Read: " + str( my_current ) + ")" )
        errors += 1
    device.setNextState(IDLE_STATE)
    for i in range( 0 , 5 ) :
	    device.run_timestep( simlist )
    my_current = device.getState().getParam('current')
    if my_current != 18.0 :
        print( "IDLE_STATE current is incorrect! (Read: " + str( my_current ) + ")" )
        errors += 1
    device.setNextState( RX_STATE )
    device.run_timestep( simlist )
    my_current = device.getState().getParam('current')
    if my_current != -10000.0 :
        print( "RX_STATE current is incorrect! (Read: " + str( my_current ) + ")" )
        errors += 1
    print( "Number of errors: " + str( errors ) )

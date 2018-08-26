#!/usr/bin/env python3

"""@package Simulated 
The simulated module contains the Simulated class that is an abstract class
that generalizes the notions fo a device, central hub, anchor and node. It 
also contains the ActionQueue class that is resposuble for keeping track of
the current stated of the actions that are waiting to be executed (time until
execution).
"""

#############
## Imports ##
#############
import types
from abc import ABC , abstractmethod
from action import Action
import sys

DEBUG = True


#############
## Classes ##
#############
class Simulated( ABC ) :
	#Jesse added code
	def __init__( self ):
		self.actionQueue = ActionQueue( )

	# Note: Should be protected method, but Python mangles
	# names of __ methods, so you can't implement them in subclasses.
	@abstractmethod
	def mainloop( self, simlist: list ) :
		pass

	def run_timestep( self , simlist : list ):
		self.mainloop( simlist )
		self.actionQueue.update( )

class ActionQueue():
	"""
	Creates instance of Action Queue
	"""
	
	def __init__( self ):
		self.queue = list( )
		
	def addToQueue( self, newAction : Action ):
		"""
		ensures action was passed in to be added to the queue
		if not, it will fail and return 
		"""
		
		try:
			assert( isinstance( newAction, Action ) )
		except:
			print("simulated.addToQueue (Please pass action to add to queue ( : )")
			raise 

		self.queue.append( newAction )
		
	def popAction( self ):
		"""
		removes the oldest Action from the list
		"""
		del( self.queue[0] )
		
	
	def update( self ):
		"""
		Every time the update function is called, decrement the counter of 
		the first action in the action queue. If the the counter is zero, 
		pop the action off the action queue
		"""
		
		if len( self.queue ) == 0:
			if DEBUG:
				print("there are no items in the action queue")
			pass
		else:
			self.queue[0].decrement( )
			if self.queue[0].get_ctr( ) == 0:
				self.popAction( )


	def test( self, test ):
		"""
		Arbitrary function added for unit test. 
		"""
		print( test )

	
	
	
if __name__ == '__main__':
	#unit test

	errors = 0
	#Create instance of ActionQueue
	aq = ActionQueue( )

	print( len( aq.queue ) )

	#ensure that non Action types cannot be added to queue	
	try:
		aq.addToQueue( 111 )
		print( "darn, the action was added" )
		errors += 1
	except:
		print( "The action was not added, way to go!" )

	#ensure that valid actions can be added
	try:
		action1 = Action( aq.test, ["I was the first action added"] )
		action1.set_ctr(3)
		aq.addToQueue( action1 )
		print( "A valid action was added to the action queue" )
		print( "The current length of the queue is" ,  len( aq.queue ) ) 
	except:
		print( "Fix Could not add a valid action to queue" )
		errors += 1 

	#ensure that the update function runs the approriate number of times (3)
	for i in range ( 0,3 ):
		print ( "call", i + 1 ) 
		aq.update( ) 
	if i + 1 != 3:
		print(" update should have been called 3 times but was called", i + 1, "times" )

	
	#add multiple actions and ensure the queue is in the correct order
	print( "The current length of the queue is" ,  len( aq.queue ) )
	action1 = Action( aq.test, ["I should be first"] )
	action1.set_ctr( 3 )
	action2 = Action( aq.test, ["then me (:"] )
	action2.set_ctr( 10 ) 
	action3 = Action( aq.test, ["lastly me (;"] )
	action3.set_ctr( 7 )
	aq.addToQueue( action1 )
	aq.addToQueue( action2 )
	aq.addToQueue( action3 )
	
	
	print( "The current length of the queue is" ,  len( aq.queue ) )
	
	while len( aq.queue ) != 0:
		i = 0
		while aq.queue[0].get_ctr( ) != 1:
			i += 1
			aq.update( )
		i += 1
		aq.update( )
		print("update was called", i, "times")

	# #ensure that update() doesn't break if empty queue
	aq.update()

	print( "===================" )
	print( "Unit test complete." )
	print( "Number of errors:",  errors )
	print( "===================" )
	sys.exit( errors )

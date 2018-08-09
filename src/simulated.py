#!/usr/bin/env python3

#############
## Imports ##
#############
from abc import ABC
from action import Action


#############
## Classes ##
#############
class Simulated( ABC ) :
	pass


class ActionQueue():
	"""
	Creates instance of Action Queue
	"""
	
	def __init__(self):
		self.queue = list()
		
	def addToQueue(self, newAction):
		assert isinstance(newAction, Action)
		self.queue.append(newAction)
		
	def popAction(self):
		return self.queue.pop()
	
	def test(self, test):
		print("test")
	
	
if __name__ == '__main__':
	aq = ActionQueue()
	print(len(aq.queue))
	aq.addToQueue(Action(aq.test, ["hello"]))
	print(len(aq.queue))
	function = aq.queue[0].get_fn()
	function(aq.queue[0].get_args())
	aq.popAction()
	print(len(aq.queue))
	
	
	
	
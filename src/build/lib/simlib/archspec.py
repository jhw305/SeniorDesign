#!/usr/bin/env python3

"""@package Architecture Specification
This module presents the simulation environment with the types of the hub, nodes, and
anchors.
"""

#############
## Imports ##
#############
import simulated

#############
## Classes ##
#############
class ArchSpec :
	"""
	Architecture specification
	Defines what classes to use for hub, anchors, and nodes.
	"""
	# Constructors

	"""
	The default constructor
	@param hubclass The type of the central hub
	@param anchorclass The type of the anchor
	@param nodeclass The type of the node
	"""
	def __init__( self , hubclass : type , anchorclass : type , nodeclass : type ) -> None :
		self.set_hubclass( hubclass )
		self.set_anchorclass( anchorclass )
		self.set_nodeclass( nodeclass )

	# Getter methods

	"""
	Returns the type of the central hub
	"""
	def get_hubclass( self ) -> type :
		return self.__hubclass

	"""
	Returns the type of the anchor
	"""
	def get_anchorclass( self ) -> type :
		return self.__anchorclass

	"""
	Returns the type of the node
	"""
	def get_nodeclass( self ) -> type :
		return self.__nodeclass

	# Setter methods

	"""
	Assigns the type of the hub. Checks whether the type inherits Simulated.
	@param hubclass Type of the central hub
	"""
	def set_hubclass( self , hubclass : type ) -> None :
		assert issubclass( hubclass , simulated.Simulated )
		self.__hubclass = hubclass

	"""
	Assigns the type of the anchor. Checks whether the type inherits Simulated.
	@param anchorclass Type of the central anchor
	"""
	def set_anchorclass( self , anchorclass : type ) -> None :
		assert issubclass( anchorclass , simulated.Simulated )
		self.__anchorclass = anchorclass

	"""
	Assigns the type of the node. Checks whether the type inherits Simulated.
	@param nodeclass Type of the central node
	"""
	def set_nodeclass( self , nodeclass : type ) -> None :
		assert issubclass( nodeclass , simulated.Simulated )
		self.__nodeclass = nodeclass

	""" @var __hubclass
	The type of the central hub
	"""
	""" @var __anchorclass
	The type of the anchors
	"""
	""" @var __nodeclass
	The type of the nodes
	"""

if __name__ == "__main__" :

	errors = 0
	
	# Test with bogus types
	try :
		archspec_obj = ArchSpec( int , int , int )
		print( "Types do not need to inherit Simulated!" )
		errors += 1
	except AssertionError :
		print( "Great! All types must inherit Simulated!" )
	# Create a custom subclass
	class MySubclass( simulated.Simulated ) :
		pass
	# Test with mysubclass
	try :
		archspec_obj = ArchSpec( MySubclass , MySubclass , MySubclass )
		print( "Perfect! Can assign Simulated child classes." )
	except AssertionError :
		print( "Cannot assign Simulated child classes." )
		errors += 1

	print( "===============" )
	print( "Finished unit test" )
	print( "Errors: " + str( errors ) )
	print( "===============" )

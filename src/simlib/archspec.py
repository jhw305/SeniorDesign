#!/usr/bin/env python3

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

	def __init__( self , hubclass : type , anchorclass : type , nodeclass : type , anchor_separation : int = 0 , anchor_to_hub_distance : int = 0 ) :
		self.set_hubclass( hubclass )
		self.set_anchorclass( anchorclass )
		self.set_nodeclass( nodeclass )
		self.set_anchor_separation( anchor_separation )
		self.set_anchor_to_hub_distance( anchor_to_hub_distance )

	# Getter methods

	def get_anchor_separation( self ) :
		return self.__anchor_separation

	def get_anchor_to_hub_distance( self ) :
		return self.__anchor_to_hub_distance

	def get_hubclass( self ) :
		return self.__hubclass

	def get_anchorclass( self ) :
		return self.__anchorclass

	def get_nodeclass( self ) :
		return self.__nodeclass

	# Setter methods

	def set_anchor_separation( self , anchor_separation : int ) :
		assert anchor_separation >= 0
		self.__anchor_separation = anchor_separation

	def set_anchor_to_hub_distance( self , anchor_to_hub_distance : int ) :
		assert anchor_to_hub_distance >= 0
		self.__anchor_to_hub_distance = anchor_to_hub_distance

	def set_hubclass( self , hubclass : type ) :
		assert issubclass( hubclass , simulated.Simulated )
		self.__hubclass = hubclass

	def set_anchorclass( self , anchorclass : type ) :
		assert issubclass( anchorclass , simulated.Simulated )
		self.__anchorclass = anchorclass

	def set_nodeclass( self , nodeclass : type ) :
		assert issubclass( nodeclass , simulated.Simulated )
		self.__nodeclass = nodeclass

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

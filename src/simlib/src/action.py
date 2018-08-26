#!/usr/bin/env python3

import sys

"""@package Action
This module defines the Action object, which is used, together with the ActionQueue class,
to implement delayed function calls.
"""

# Note: Only currently supports Python3

#############
## Imports ##
#############
import types
from inspect import signature

#############
## Classes ##
#############

# Action Class
class Action :
	"""
	Element of an action queue
	"""
	
	# Constructors
	
	def __init__( self , fn_to_be_called : types.FunctionType , fn_arg_list : list  , ctr_val : int = 0 ) -> None :
		"""
		Default constructor
		The number of arguments is checked. It is fn_to_be_called's responsibility
		to check the types of the arguments.

		@param fn_to_be_called Function to be called (mandatory)
		@param fn_arg_list List of function arguments (mandatory)
		@param ctr_val Counter value (default to 0; optional)
		"""
		self.set_fn( fn_to_be_called , fn_arg_list )
		self.set_ctr( ctr_val )

	# Useful methods

	def decrement( self , n : int = 1 ) -> None :
		"""
		Decrement the counter by n, defaulted to 1.
		If the counter should be 0 or lower, it will not drop below 0.
		Instead, call the function with the associated arguments and
		set the counter to 0.
		@param n The amount by which the counter is decremented
		"""
		assert n >= 0
		self.__ctr_val -= n
		if self.__ctr_val <= 0 :
			self.__ctr_val = 0
			self.__fn_to_be_called( *self.__fn_arg_list )

	# Setter methods

	def set_fn( self , fn_to_be_called : types.FunctionType , fn_arg_list : list ) -> None :
		"""
		Assigned function to be called and the argument list.
		Number of args is checked. fn_to_be_called will need to check types of args.
		@param fn_to_be_called Function to be called
		@param fn_arg_list List of arguments passed to fn_to_be_called
		"""
		assert len( signature( fn_to_be_called ).parameters ) == len( fn_arg_list )
		self.__fn_to_be_called = fn_to_be_called
		self.__fn_arg_list = fn_arg_list

	def set_ctr( self , ctr_val : int ) -> None :
		"""
		Checks that ctr_val is 0 or greater, and sets the counter value accordingly.
		@param ctr_val The new counter value
		"""
		assert ctr_val >= 0
		self.__ctr_val = ctr_val

	# Getter methods

	def get_fn( self ) -> types.FunctionType :
		"""
		Returns the function associated with this action.
		"""
		return self.__fn_to_be_called

	def get_args( self ) -> list :
		"""
		Returns the function args associated with this action.
		"""
		return self.__fn_arg_list

	def get_ctr( self ) -> int :
		"""
		Returns the counter value associated with this action.
		"""
		return self.__ctr_val

if __name__ == "__main__" :
	# Unit Test
	errors = 0
	
	# Test function
	def fn( n ) :
		print( "Current value of n: " + str( n ) )

	# Initialize action object
	test_obj = None
	try :
		test_obj = Action( )
		print( "Action doesn't break if instantiated with wrong number of args!" )
		errors += 1
	except TypeError :
		print( "Great! Action breaks if instantiated with wrong number of args!" )
	# Set function args
	test_obj = Action( fn , [ 1 ] )
	# Test decrement when ctr is 0
	print( "We should now see the function be called." )
	test_obj.decrement( )
	# Test getters
	print( "Testing getters" )
	print( "Function object: " + str( test_obj.get_fn( ) ) )
	print( "Args: " + str( test_obj.get_args( ) ) )
	if test_obj.get_args( ) != [ 1 ] :
		print( "Wrong args!" )
		errors += 1
	print( "Ctr: " + str( test_obj.get_ctr( ) ) )
	if test_obj.get_ctr( ) != 0 :
		print( "Wrong counter val!" )
		errors += 1
	# Call setters and reset the counter
	def fn2( x , y ) :
		print( "New string: " + str( x + y ) )
	test_obj.set_fn( fn2 , [ 1 , 3 ] )
	if test_obj.get_args( ) != [ 1 , 3 ] :
		print( "Wrong args!" )
		errors += 1
	test_obj.set_ctr( 3 )
	if test_obj.get_ctr( ) != 3 :
		print( "Wrong ctr!" )
		errors += 1
	# Decrement a few times until function is called
	test_obj.decrement( )
	print( "We should now see the function be called." )
	test_obj.decrement( 5 )
	if test_obj.get_ctr( ) != 0 :
		print( "Wrong ctr!" )
		errors += 1
	# Test constructor with optional argument
	test_obj = Action( fn , [ 3 ] , 3 )
	if test_obj.get_ctr( ) != 3 :
		print( "Wrong ctr!" )
		errors += 1
	if test_obj.get_args( ) != [ 3 ] :
		print( "Wrong args!" )
		errors += 1

	print( "===================" )
	print( "Unit test complete." )
	print( "Number of errors: " + str( errors ) )
	print( "===================" )

	sys.exit( errors )

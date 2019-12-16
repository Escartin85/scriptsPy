class Borg:
	#Borg class making class attributes global
	_shared_state = {}		# Attribute dictionary

	def __init__(self):
		# Naje ut ab attrubute dictionary
		self.__dict__ = self._shared_state

# Inherits from the Borg class
class Singleton():
	# This essenstially makes the singleton objects an object-oriented global variables
	def __init__(self, **kwargs):
		Borg.__init__(self)
		# Update the attribute dictionary by inserting a new key-value pair
		self._shared_state.update(kwargs)

	def __str__(self):
		# Returns the attribute dictionary for printing
		return str(self._shared_state)

# Create a singleton object and add out first acronym
singleton = Singleton(HTTP = "Hyper Text Transfer Protocol")

# Print the object
print(singleton)

# Create another singleton object and if it refers to the same attribute dictionary by adding another acronym
singleton2 = Singleton(SNMP = "Simple Network Management Protocol")

# Print the object
print(singleton2)
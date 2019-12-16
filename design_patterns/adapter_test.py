# Class Spanish speaker
class Spanish:
	def __init__(self):
		self.name = "Spanish"

	def speak_spanish(self):
		return "Hola amigo!"

# Class British speaker
class British:
	def __init__(self):
		self.name = "British"

	# The different method name here
	def speak_english(self):
		return "Hello my friend!"

# This changes the generic method name to individualized method names
class Adapter:
	# Change the name of the method
	def __init__(self, object, **adapted_method):
		self._object = object

		# Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		# for example, speak() will be translated to speak_spanish() if the mapping says so
		self.__dict__.update(adapted_method)

	# Simply return the rest of atrributes
	def __getattr__(self, attr):
		return getattr(self._object, attr)

# List to store speaker objects
objects = []

# Create a Spanish object
spanish = Spanish()

# Create a British object
british = British()

# Append the objects to the object list
objects.append(Adapter(spanish, speak=spanish.speak_spanish))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
	print("{} says '{}'\n".format(obj.name, obj.speak()))
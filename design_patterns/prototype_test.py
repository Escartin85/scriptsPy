import copy

class Prototype:

	def __init__(self):
		self._objects = {}

	# Register an object
	def register_object(self, name, obj):
		self._objects[name] = obj

	# Unregister an object
	def unregister_object(self, name):
		del self._objects[name]

	# Clone a registered object and update its attributes
	def clone(self, name, **attr):
		obj = copy.deepcopy(self._objects.get(name))
		obj.__dict__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.name = "Bmw"
		self.color = "Red"
		self.options = "Ex"

	def __str__(self):
		return '{} | {} | {}'.format(self.name, self.color, self.options)


# Test class

car = Car()
prototype = Prototype()
prototype.register_object('bmw', car)

carClone = prototype.clone('bmw')

print(carClone)
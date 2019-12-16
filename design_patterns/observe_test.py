# Represents what is being 'observed'
class Subject(object):
	# This where references to all the observers are being kept
	# Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers
	def __init__(self):
		self._observers = []

	# If the observer is not already in the observers list
	# append the observer to the list
	def attach(self, observer):
		if observer not in self._observers:
			self._observers.append(observer)

	# Simply remove the observer
	def detach(self, observer):
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	# For all the observer in the list
	# Don't notify the observer who is actually updating the temperature
	# Alert the observers
	def notify(self, modifier=None):
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

# Inherits from the Subject class
class Core(Subject):
	def __init__(self, name=""):
		Subject.__init__(self)
		# Set the name of the core
		self._name = name
		# Initialize the temperature of the core
		self._temp = 0

	# Getter that gets the core temperature
	@property
	def temp(self):
		return self._temp
	
	# Setter that gets the core temperature
	@temp.setter
	def temp(self, temp):
		self._temp = temp
		# Notify the observer whenever somebody changes the core temperature
		self.notify()

class TempViewer:
	# Alert method that is invoked when the notify() method in a concrete subject is invoked
	def update(self, subject):
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Create our observers
v1 = TempViewer()
v2 = TempViewer()

# Attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Change the temperature of our first core
c1.temp = 80
c1.temp = 90

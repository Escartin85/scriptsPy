# The class being visited
class House(object):
	# Interface the visiting operation
	# Trigger the visitor operation
	def accept(self, visitor):
		visitor.visit(self)

	# Note that we now have a reference to the HVAC specialist object in the house object
	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist)

	# Note that we now have a reference to the electrician object in the house object
	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician)

	# Simply return the class name when the House object is printed
	def __str__(self):
		return self.__class__.__name__

# Abstract visitor
class Visitor(object):
	# Simply return the class name when the Visitor object is printed
	def __str__(self):
		return self.__class__.__name__

# Inherits from the parent class, Visitor
class HvacSpecialist(Visitor):
	# Note that the visitor now has a reference to the house object
	def visit(self, house):
		house.work_on_hvac(self)

# Inherits from the parent class, Visitor
class Electrician(Visitor):
	# Note that the visitor now has a reference to the house object
	def visit(self, house):
		house.work_on_electricity(self)


# Create a HVAC specialist
hv = HvacSpecialist()

# Create an electrician
e = Electrician()

# Create a house
home = House()

# The house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)

# The house accept the electrician specialist and work on the house by invoking the visit() method
home.accept(e)
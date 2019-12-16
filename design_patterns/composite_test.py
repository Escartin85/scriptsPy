# Abstract class
class Component(object):
	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

# Inherits from the abstract class, Component
# Component class
class Child(Component):
	# Concrete class
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		# This is where we store the name of your child item!
		self.name = args[0]

	# Print the name of your child item here
	def component_function(self):
		print("{}".format(self.name))

# Inherits from the abstract class, Component
class Composite(Component):
	# Concrete class and maintains the three recursive structure
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		# This is where we store the name of the composite object
		self.name = args[0]
		# This is where we keep our child items
		self.children = []


	# Methos to add a new child item
	def append_child(self, child):
		self.children.append(child)

	# Method to remove a child item
	def remove_child(self, child):
		self.children.remove(child)

	def component_function(self):
		# Print the name of the compositve object
		print("{}".format(self.name))

		# Iterate through the child objects and invoke their component function printing their names
		for child in self.children:
			child.component_function()


# Build a composite submenu 1
sub1 = Composite("-submenu1")

# Create a new child sub_submenu 11
sub11 = Child("--sub_submenu 11")

# Create a new child sub_submenu 12
sub12 = Child("--sub_submenu 12")

# Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)

# Add the sub_submenu 12 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("top_menu")

# Create a new child sub_submenu 11
sub2 = Child("-submenu2")

# Add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

# Add the sub_submenu 12 to submenu 1
top.append_child(sub2)

# Test if our Composite pattern works
top.component_function()
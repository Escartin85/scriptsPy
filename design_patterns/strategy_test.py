import types

# The Strategy Pattern class
class Strategy:
	def __init__(self, function=None):
		self.name = "Default Strategy"

		# If a reference to a function is provided, replace the execute() method with the given function
		if function:
			self.execute = types.MethodType(function, self)

	# This gets replaced by abother version if another strategy is provided
	# The default method that prints the name of the strategy being used
	def execute(self):
		print("{} is used!".format(self.name))

# Replacement method 1
def strategy_one(self):
	print("{} is used to execute method 1".format(self.name))

# Replacement method 2
def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))


# Create our default strategy
s0 = Strategy()

# Execute our default strategy
s0.execute()

# Create the first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)

# Set its name
s1.name = "Strategy One"

# Execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
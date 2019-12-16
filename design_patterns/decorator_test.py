from functools import wraps

# Define the decorator
def make_blink(function):

	# This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	# Define the inner function
	def decorator():
		# Grab the return value of the function bein decorated
		ret = function()

		# Add new functionality to the function being decorated
		return "<span>" + ret + "</span>"

	return decorator

# Apply the decorator here!
@make_blink
def hello_world():
	""" Original coment function """

	return "This is the world!!"


print(hello_world())

print(hello_world.__name__)

print(hello_world.__doc__)
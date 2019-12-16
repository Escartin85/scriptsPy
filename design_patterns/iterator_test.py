# Out iterator implementation
def count_to(count):
	# Out list
	numbers_in_spanish = ["uno", "dos", "tres", "cuatro", "cinco"]

	# Out built-in iterator
	# Create a tuple such as (1, "uno")
	iterator = zip(range(count), numbers_in_spanish)

	# Iterate through our iterable list
	# Extract the Spanish numbers
	# Put them in a generator called number
	for position, number in iterator:
		# Return a 'generator' containing numbers in Spanish
		yield number

# Test the generator returned by our iterator
for num in count_to(3):
	print("{}".format(num))
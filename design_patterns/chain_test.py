# Abstract handler
class Handler:
	# Define who is the next handler
	def __init__(self, successor):
		self._successor = successor

	def handle(self, request):
		# If handled, stop here
		handled = self._handle(request)

		# Otherwise, keep going
		if not handled:
			self._successor.handle(request)

	def _handle(self, request):
		raise NotImplementedError("Must provide implementation in subclass!")

#Inherit from the abstract handler
class ConcreteHandler1(Handler):
	def _handle(self, request):
		# Provide a condition for handling
		if 0 < request <= 10:
			print("Request {} handler in handler 1".format(request))
			# Indicates that the request has been handled
			return True

#Inherit from the abstract handler
class DefaultHandler(Handler):
	def _handle(self, request):
		# If there is no handler available
		# No condition checking since this is a default handler
		print("End of chain, no handler for {}".format(request))
		# Indicates that the request has been handled
		return True

class Client:
	# Using handlers
	def __init__(self):
		# Create handlers and use them in a sequence you want
		self.handler = ConcreteHandler1(DefaultHandler(None))
		# Note that the default handler has no successor

	# Send your requests one at a time for handlers to handle
	def delegate(self, requests):
		for request in requests:
			self.handler.handle(request)


# Create a client
client = Client()

# Create a request
requests = [2, 5, 30]

# Send the requests
client.delegate(requests)
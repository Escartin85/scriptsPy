import time

# Define the 'resource-intensive' object to instantiatel
class Producer:
	def producer(self):
		print("Producer is working!")

	def meet(self):
		print("Producer has time to meet you!")

# Define the 'relativily less resource-intensive' proxy to instantiate as middleman
class Proxy:
	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		print("Artist checking if Producer is available...")

		
		if self.occupied == 'No':
			# If the producer is available, create a producer object
			self.producer = Producer()
			time.sleep(2)

			# Make the producer meet the guest
			self.producer.meet()

		else:
			# Otherwise, don't instantiate a produce
			time.sleep(2)
			print("Producer is busy!!")


# Instantiate a Proxy
proxy = Proxy()

# Make the Proxy: Artist produce until Producer is available
proxy.produce()

# Change the state to 'occupied'
proxy.occupied = 'Yes'

# Make the Producer produce
proxy.produce()
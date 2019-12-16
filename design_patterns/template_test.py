import sys

from abc import ABC, abstractmethod

# This class inherit from Abstract Base Class to allow the use of the @abstractmethod decorator
class AbstractClass(ABC):

	# This is the template method that contains a collection of methods to stay the same,
	# and to be overriden optionally
	def template_method(self):
		self.__always_do_this()
		self.do_step_1()
		self.do_step_2()
		self.do_this_or()
	# This is a protected method that should not be overriden
	def __always_do_this(self):
		name = sys._getframe().f_code.co_name
		print('{}'.format(self.__class__.__name__, name))

	# This method should be overriden
	@abstractmethod
	def do_step_1(self):
		pass

	# This method should be overriden
	@abstractmethod
	def do_step_2(self):
		pass

	def do_this_or(self):
		print('You can overide me but you don not have to')

# This class inherit from Abstract Class featuring the template method
class ConcreteClassA(AbstractClass):

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassA ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassA ...')

# This class inherit from Abstract Class featuring the template method
class ConcreteClassB(AbstractClass):

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassB ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassB ...')

	def do_this_or(self):
		print('Doing my own business...')

def main():
	
	print("== ConcreteClassA ==")
	a = ConcreteClassA()
	a.template_method()

	print("== ConcreteClassB ==")
	b = ConcreteClassB()
	b.template_method()


if __name__ == "__main__":
	main()
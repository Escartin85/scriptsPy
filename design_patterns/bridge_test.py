# Implementation-specific abstraction: concrete class one
class DrawingAPIone(object):
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

# Implementation-specific abstraction: concrete class two
class DrawingAPItwo(object):
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

# Implementation-independent abstraction: for example, there could be a ractangle class!
class Circle(object):
	# Initialize the necessary attributes
	def __init__(self, x, y, radius, drawing_api):
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	# Implementation-specific abstraction taken care of by another class: DrawingAPI
	def draw(self):
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	# Implementation-independent
	def scale(self, percent):
		self._radius *= percent

# Build the first Circle object using API one
circle = Circle(1, 2, 3, DrawingAPIone())

# Draw a circle
circle.draw()

# Build the second Circle object using API two
circle2 = Circle(2, 3, 4, DrawingAPItwo())

# Draw a circle
circle2.draw()
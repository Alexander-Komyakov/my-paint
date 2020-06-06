#/usr/bin/env python3

class Pencil:
	def __init__(self, width, height, color):
		self.color = color
		self.width = width
		self.height = height

	def draw(self, screen, x, y):
		screen.fill(self.color, (x, y, self.width, self.height))

	def get_width(self):
		return self.width
	def get_height(self):
		return self.height

	def get_color(self):
		return self.color
	def set_color(self, color):
		self.color = color
	
	def set_width(self, width):
		self.width = width
	def set_height(self, height):
		self.height = height

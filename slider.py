#!/usr/bin/env python3
import pygame

class Slider:
	def __init__(self, x, y, width, height, color, color_button):
		self.x = x; self.y = y
		self.color = color; self.color_button = color_button
		self.width = width
		self.height = height
		self.x_button = int(self.x + width / 2)
		self.y_button = self.y
		self.color_button = color_button
		self.width_button = int(width / 10)
		self.height_button = height
		self.value = 0.5
	def collision(self, mouse_x, mouse_y):
		if (mouse_x >= self.x and 
			mouse_x <= self.x + self.width - self.width_button
			and mouse_y >= self.y and mouse_y <= self.y + self.height):
			return True
		else:
			return False
	def move(self, mouse_x, mouse_y, mouse_but_down):
		if (self.collision(mouse_x, mouse_y) and (mouse_but_down == (1, 0, 0))):
			self.x_button = mouse_x
			self.value = (self.x_button - self.x) / (self.width - self.width_button)
		return self.value

	def move_absolute(self, value):
		self.value = value
		self.x_button = self.value*(self.width-self.width_button)+self.x

		return self.value
	def blit(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
		pygame.draw.rect(screen, self.color_button, 
					(self.x_button, self.y_button, self.width_button, self.height_button))

#!/usr/bin/env python3

import pygame

class Button:
	def __init__(self, x, y, width, height, color, color_text, abc):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.color_text = color_text
		self.border_radius = int(self.width/10)

		self.abc = abc
		self.text_size = int(self.width*1.5)
		self.font = pygame.font.Font(None, self.text_size)
		self.text = self.font.render(self.abc, False, self.color_text)
		self.text_x = self.x + self.width/7
		self.text_y = self.y + self.height/10
	
	def collision(self, mouse_x, mouse_y, mouse_button_down):
		if (mouse_x >= self.x and mouse_x <= self.x + self.width and
			mouse_y >= self.y and mouse_y <= self.y + self.height and
			mouse_button_down == (1, 0, 0)):
			return True
		return False
	def blit(self, screen):
		pygame.draw.rect(screen, self.color, 
						(self.x, self.y, self.width, self.height))
		screen.blit(self.text, (self.text_x, self.text_y))

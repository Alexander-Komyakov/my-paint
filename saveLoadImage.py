#!/usr/bin/env python3

import pygame, copy, os
from tkinter import filedialog as fd

def SaveImage(image):
	image_name = fd.asksaveasfilename(filetypes=(("PNG files", "*.png"),
												("JPEG files", "*.jpg"),
												("All files", "*,*") ))
	if image_name != "":
		pygame.image.save(image, image_name)
def LoadImage(screen, x, y):
	image_name = fd.askopenfilename(filetypes=(("PNG files", "*.png"),
												("JPEG files", "*.jpg"),
												("All files", "*,*") ))
	if (image_name != ()):
		if (os.path.exists(image_name)):
			image = pygame.image.load(image_name)
			screen.blit(image, (x, y))


class Screenshot:
	def __init__(self, x, y, width, height, color_frame):
		self.x = x + int(width / 20)
		self.y = y + int(width / 20)
		self.width = width - int(width / 10)
		self.height = height - int(height / 10)
		self.color_frame = color_frame
	def get_image(self):
		return self.image
	def set_image(self, image):
		self.image = copy.copy(image)
		self.image_little = self.resize_image(image)
	def resize_image(self, image):
		return pygame.transform.scale(image, (self.width, self.height))
	def blit(self, screen):
		screen.blit(self.image_little, (self.x, self.y))
		pygame.draw.rect(screen, self.color_frame, (self.x, self.y, self.width, self.height), int(self.width/40))
	def load_image(self, screen, x, y):
		screen.fill((255, 255, 255))
		screen.blit(self.get_image(), (x, y))

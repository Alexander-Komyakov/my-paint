#!/usr/bin/env python3

import time, pygame
from tkinter import *
from tkinter import filedialog as fd
# здесь определяются константы, классы и функции

class Slider:
	def __init__(self, pos_x, pos_y, size_x, size_y, color, color_but):
		self.pos_x = pos_x; self.pos_y = pos_y
		self.size_x = size_x; self.size_y = size_y
		self.color = color
		self.pos_x_but = int(pos_x + size_x / 2)
		self.pos_y_but = pos_y
		self.color_but = color_but
		self.size_x_but = int(size_x / 10)
		self.size_y_but = size_y
		self.pos = 127
	def Collision(self, x, y):
		if ((x >= self.pos_x and x <= self.pos_x + self.size_x - self.size_x_but) and
			(y >= self.pos_y and y <= self.pos_y + self.size_y)):
			self.pos_x_but = x
			self.pos = (self.pos_x_but - self.pos_x) / (self.size_x - self.size_x_but)
			return True

WIDTH = 600
HEIGHT = 400

FPS = 1200 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

BACKGROUND_COLOR = WHITE

# используется
pencil_use = False #кисть
eraser_use = False # ластик

#параметры ластика
eraser_size_x = 4
eraser_size_y = 4

# параметры кисти
pencil_size_x = 4
pencil_size_y = 4

# цвет карандаша
pencil_color = [127, 127, 127]

# здесь происходит инициация, создание объектов и др.

# слайдеры
sliders = dict()
# цвет кисти
sliders["color_r"] = Slider(5, 20, 80, 15, (255, 0, 0), (0, 0, 255))
sliders["color_g"] = Slider(5, 40, 80, 15, (0, 255, 0), (255, 0, 0))
sliders["color_b"] = Slider(5, 60, 80, 15, (0, 0, 255), (255, 0, 0))
#размер карандаша
sliders["pencil_size_x"] = Slider(5, 170, 80, 15, (0, 0, 0), (255, 0, 0))
sliders["pencil_size_y"] = Slider(5, 190, 80, 15, (0, 0, 0), (255, 0, 0))
#размер ластика
sliders["eraser_size_x"] = Slider(5, 250, 80, 15, (0, 0, 0), (255, 0, 0))
sliders["eraser_size_y"] = Slider(5, 270, 80, 15, (0, 0, 0), (255, 0, 0))

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

screen.fill(BACKGROUND_COLOR)
# главный цикл
while True:

    # задержка
	clock.tick(FPS)
	#screen.fill(WHITE)

    # цикл обработки событий
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()

		elif i.type == pygame.KEYDOWN:
			if (i.key == pygame.K_s):
				rect = pygame.Rect(95, 0, WIDTH-95, HEIGHT)
				sub = screen.subsurface(rect)
				file_name = fd.asksaveasfilename(filetypes=(("PNG files", "*.png"),
                                        ("JPG files", "*.jpg;"),
                                                ("All files", "*.*") ))
				pygame.image.save(sub, file_name)
			elif (i.key == pygame.K_l):
				file_name = fd.askopenfilename()
				image_load = pygame.image.load(file_name)
				screen.blit(image_load, (95, 0, 0, HEIGHT))
		elif i.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed() == (1, 0, 0):
				pencil_use = True
			elif pygame.mouse.get_pressed() == (0, 0, 1):
				eraser_use = True
		elif i.type == pygame.MOUSEBUTTONUP:
			pencil_use = False
			eraser_use = False

	screen.fill((225, 225, 245), (0, 0, 95, HEIGHT))
	if (pencil_use):
		# изменение цвета
		if (sliders.get("color_r").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			pencil_color[0] = int(255 * sliders.get("color_r").pos)
		elif (sliders.get("color_g").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			pencil_color[1] = int(255 * sliders.get("color_g").pos)
		elif (sliders.get("color_b").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			pencil_color[2] = int(255 * sliders.get("color_b").pos)

		# изменение размера карандаша
		elif (sliders.get("pencil_size_x").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			pencil_size_x = int(sliders.get("pencil_size_x").pos * 30)
		elif (sliders.get("pencil_size_y").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			pencil_size_y = int(sliders.get("pencil_size_y").pos * 30)

		# изменение размера ластика
		elif (sliders.get("eraser_size_x").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			eraser_size_x = int(sliders.get("eraser_size_x").pos * 30)
		elif (sliders.get("eraser_size_y").Collision(pygame.mouse.get_pos()[0], 
				pygame.mouse.get_pos()[1])):
			eraser_size_y = int(sliders.get("eraser_size_y").pos * 30)

		# раскраска пикселей 
		screen.fill(pencil_color, ((pygame.mouse.get_pos()[0], 
					pygame.mouse.get_pos()[1]), 
					(pencil_size_x, pencil_size_y)))
	elif (eraser_use):
		m_x = pygame.mouse.get_pos()[0]
		m_y = pygame.mouse.get_pos()[1]
		screen.fill(BACKGROUND_COLOR, ((pygame.mouse.get_pos()[0], 
					pygame.mouse.get_pos()[1]), (eraser_size_x, eraser_size_y)))

    # --------
    # изменение объектов и многое др.
    # --------

	# итоговый цвет
	pygame.draw.rect(screen, pencil_color, (5, 90, 80, 30))
	for i in sliders.keys():
		sl = sliders.get(i)
		pygame.draw.rect(screen, sl.color, 
						(sl.pos_x, sl.pos_y, sl.size_x, sl.size_y))
		pygame.draw.rect(screen, sl.color_but, 
						(sl.pos_x_but, sl.pos_y_but, sl.size_x_but, sl.size_y_but))

	# размер кисти/ластика визуально
	pygame.draw.rect(screen, pencil_color, (5, 210, pencil_size_x, pencil_size_y))
	pygame.draw.rect(screen, BACKGROUND_COLOR, (5, 290, eraser_size_x, eraser_size_y))
    # обновление экрана
	pygame.display.update()

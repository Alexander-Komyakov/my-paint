#!/usr/bin/env python3

import time, pygame, copy
from pencil import *
from slider import *
from button import *
from saveLoadImage import *

# Константы
WIDTH = 600
HEIGHT = 400

FPS = 1200 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (240, 240, 240)

pygame.init()

# основное окно
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# Поверхности
# рисование
canvas = pygame.Surface((int(WIDTH/1.5), HEIGHT),pygame.SRCALPHA)
# инструменты
tools = pygame.Surface((int(WIDTH/6), HEIGHT))
# отображение других изображений
screen_save = pygame.Surface((int(WIDTH/6), HEIGHT))

# создание объектов
pencil = Pencil(10, 10, BLACK)
pencil_use = False # используется ли карандаш
pipette_use = False # используется ли карандаш

save_image = [Screenshot(0, 5, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140))]
save_image.append(Screenshot(0, 5, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140)))
save_image.append(Screenshot(0, 80, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140)))
save_image.append(Screenshot(0, 155, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140)))
save_image.append(Screenshot(0, 230, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140)))
save_image.append(Screenshot(0, 305, int(WIDTH/6), int(HEIGHT/5), (140, 140, 140)))
for i in save_image:
	i.set_image(canvas)

# кнопки
buttons = dict()
buttons["Save0"] = Button(10, 15, 15, 15, (150, 150, 150), (120, 120, 120), "S")
buttons["Load0"] = Button(30, 15, 15, 15, (150, 150, 150), (120, 120, 120), "L")
buttons["Save1"] = Button(10, 90, 15, 15, (150, 150, 150), (120, 120, 120), "S")
buttons["Load1"] = Button(30, 90, 15, 15, (150, 150, 150), (120, 120, 120), "L")
buttons["Save2"] = Button(10, 165, 15, 15, (150, 150, 150), (120, 120, 120), "S")
buttons["Load2"] = Button(30, 165, 15, 15, (150, 150, 150), (120, 120, 120), "L")
buttons["Save3"] = Button(10, 240, 15, 15, (150, 150, 150), (120, 120, 120), "S")
buttons["Load3"] = Button(30, 240, 15, 15, (150, 150, 150), (120, 120, 120), "L")
buttons["Load4"] = Button(10, 315, 15, 15, (150, 150, 150), (120, 120, 120), "L")

# слайдеры
sliders = dict()
sliders["pencil_width"] = Slider(5, 15, 90, 15, BLACK, BLUE)
sliders["pencil_height"] = Slider(5, 35, 90, 15, BLACK, BLUE)

sliders["pencil_color_red"] = Slider(5, 55, 90, 15, RED, BLUE)
sliders["pencil_color_green"] = Slider(5, 75, 90, 15, GREEN, BLUE)
sliders["pencil_color_blue"] = Slider(5, 95, 90, 15, BLUE, BLACK)

# таймер
clock = pygame.time.Clock()

# раскраска поверхностей
tools.fill(GRAY)
screen_save.fill(GRAY)

window.fill(WHITE)
# прозрачность
canvas.fill
canvas.set_alpha(255)

# отображение поверхностей в окне
window.blit(tools, (0, 0))
window.blit(screen_save, (int(WIDTH-(WIDTH/6)), 0))
window.blit(canvas, (int(WIDTH/6), 0),special_flags=(pygame.BLEND_RGBA_ADD))
pygame.display.update()

# главный цикл
while True:

    # задержка
	clock.tick(FPS)

	# берем координаты мыши
	mouse_x = pygame.mouse.get_pos()[0]
	mouse_y = pygame.mouse.get_pos()[1]
	mouse_but_down = pygame.mouse.get_pressed()

	# закраска поверхностей
	tools.fill(GRAY)

    # цикл обработки событий
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()

		if i.type == pygame.KEYDOWN:
			if (i.key == pygame.K_s):
				SaveImage(canvas)
			if (i.key == pygame.K_l):
				LoadImage(canvas, 0, 0, WIDTH-WIDTH/3, HEIGHT)
		if i.type == pygame.MOUSEBUTTONDOWN:
			if (mouse_x > int(WIDTH/6) and mouse_x < int(WIDTH-(WIDTH/6)) and pygame.mouse.get_pressed() == (1, 0, 0)):
				save_image[len(save_image)-1].set_image(canvas)
				pencil.draw(canvas, mouse_x - int(WIDTH/6), mouse_y)
				pencil_use = True
			if (mouse_x > int(WIDTH/6) and mouse_x < int(WIDTH-(WIDTH/6)) and pygame.mouse.get_pressed() == (0, 1, 0)):
				pencil.set_color(window.get_at((mouse_x, mouse_y)))
				pipette_use = True

		elif i.type == pygame.MOUSEBUTTONUP:
			pencil_use = False
			pipette_use = False
		if i.type == pygame.MOUSEMOTION:
			if (pencil_use):
				pencil.draw(canvas, mouse_x - int(WIDTH/6), mouse_y)
	
	# изменение размера карандаша
	pencil.set_width(sliders.get("pencil_width").move(mouse_x, mouse_y, mouse_but_down) * 40)
	pencil.set_height(sliders.get("pencil_height").move(mouse_x, mouse_y, mouse_but_down) * 40)
	# изменение цвета
	if (pipette_use == False):
		r = sliders.get("pencil_color_red").move(mouse_x, mouse_y, mouse_but_down) * 255
		g = sliders.get("pencil_color_green").move(mouse_x, mouse_y, mouse_but_down) * 255
		b = sliders.get("pencil_color_blue").move(mouse_x, mouse_y, mouse_but_down) * 255
		pencil.set_color( (r, g, b) )
	else:
		sliders.get("pencil_color_red").move_absolute(pencil.get_color()[0] / 255)
		sliders.get("pencil_color_green").move_absolute(pencil.get_color()[1] / 255)
		sliders.get("pencil_color_blue").move_absolute(pencil.get_color()[2] / 255)

	# сохранение/загрузка картинок в правой панели
	# координаты относительно tools: mouse_x-(WIDTH/1.2)

	for i in range(0, 4):
		if (buttons.get("Save"+str(i)).collision(mouse_x-(WIDTH/1.2), mouse_y, mouse_but_down)):
			save_image[i+1].set_image(canvas)
		if (buttons.get("Load"+str(i)).collision(mouse_x-(WIDTH/1.2), mouse_y, mouse_but_down)):
			save_image[i+1].load_image(canvas, 0, 0)
	if buttons.get("Load4").collision(mouse_x-(WIDTH/1.2), mouse_y, mouse_but_down):
		save_image[5].load_image(canvas, 0, 0)


	# отрисовка слайдеров	
	for i in sliders.keys():
		sl = sliders.get(i)
		sl.blit(tools)
	# отрисовка кнопок
	for i in buttons.keys():
		but = buttons.get(i)
		but.blit(screen_save)
	# итоговый размер и цвет кисти
	pygame.draw.rect(tools, pencil.get_color(), (5, 120, int(pencil.width), int(pencil.height)))

	# отображение поверхностей в окне
	window.blit(tools, (0, 0))
	window.blit(screen_save, (int(WIDTH-(WIDTH/6)), 0))
	window.blit(canvas, (int(WIDTH/6), 0))

	for i in save_image:
		i.blit(screen_save)

    # обновление экрана
	pygame.display.update((0, 0, int(WIDTH/6), HEIGHT))
	pygame.display.update((WIDTH - int(WIDTH/6), 0, int(WIDTH/6), HEIGHT))
	pygame.display.update((int(WIDTH/6), 0, int(WIDTH-(WIDTH/3)), HEIGHT))

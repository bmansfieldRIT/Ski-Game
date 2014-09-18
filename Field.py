"""	File: Field.py
	Author: Brian Mansfield
	This file represents the playing field of the game, containing
	all data involving what can appear on the field and what events can
	occur on the field.
"""

import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Ski Game!')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('Ski Game!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

windowSurface.blit(text, textRect)

pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

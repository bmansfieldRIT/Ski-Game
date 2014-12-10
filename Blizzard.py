"""	File: Blizzard.py
	Author: Brian Mansfield
	This file is the game loop, the main logic of the game and
	object interactions goes here.
"""

import pygame, sys, time, math, random
from pygame.locals import *

##### CONSTANTS #####

# Window
FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
WHITE = (255, 255, 255)
SNOWBACKGROUND = (255, 255, 255)
BLUE = (0, 0, 255)

# Game Constants
ENEMYMOVERATE = 9
INVULNTIME = 2      # how long after being hit
GAMEOVERTIME = 4    # how long the game over screen lasts
HEALTHSTART = 3
MAXENEMIES = 4
STARTSCREENTIME = 3
DAYLIGHT = 1
NIGHT = 0
LEFT = 'left'
RIGHT = 'right'

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        """ Constructor for Player. Passes starting x and y pos."""
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('skiman.png')
        self.rect = self.image.get_rect()

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, PLAYER_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('player.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('BLIZZARD!')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # load the image files
    PLAYER_IMG = pygame.image.load('player.png')
    DRIFTMARKS = []
    
    # for i in range(1,2):
    #   DRIFTMARKS.append(pygame.image.load('swoosh%s.png', % i))   

    while True:
        runGame()

def runGame():
    # set up variables for the start of a new game
    invulnerableMode        = False # if the player is invulnerable
    invulnerableStartTime   = 0     # time the player became invulnerable
    gameOverMode            = False # if the player has lost
    gameOverStartTime       = 0     # time the player lost

    # create the surfaces to hold game text
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    GameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf = BASICFONT.render('(Press "r" to restart', True, WHITE)
    winRect = gameOverSurf.get_rect()
    winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)



    
    # main program loop
    while not done:
            for event in pygame.event.get():
                    if event.type == QUIT:
                            done = True

                    # game logic goes here                


                    # drawing code goes here

            windowSurface.fill(WHITE)

            # sets player sprite as mouse position on screen
            pos = pygame.mouse.get_pos()
            player.rect.x = pos[0]
            player.rect.y = pos[1]
            
            primary_sprite_list.draw(windowSurface)
            clock.tick(60)
            pygame.display.flip()


    pygame.quit()
    sys.exit()

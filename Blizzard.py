"""	File: Blizzard.py
	Author: Brian Mansfield
	This file is the game loop, the main logic of the game and
	object interactions go here.
"""

import pygame, sys, time, math, random
from pygame.locals import *

##### CONSTANTS #####

# Window
FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

PLAYERIMAGE = '../images/skiman.bmp' # relative path from working directory
RAILIMAGE = '../images/rail.bmp'
RAILIMAGES = '../images/rail%s.bmp'

SNOWBACKGROUND = (255, 255, 255) # white
BLUE = (0, 0, 255)
PLAYERSIZE = 50

# Game Constants
STARTSCREENTIME = 3 # how long the start screen lasts

# X Locations for the Players and Enemies
RAIL = (WINWIDTH) / 4 # sub 25 from each side, divide into 3 rails
LEFT_RAIL = RAIL * 1
CENTER_RAIL = RAIL * 2
RIGHT_RAIL = RAIL * 3

RAILWIDTH = 10
RAILHEIGHT = 480
RAILTICK = FPS/10 # rail moves 10 times every second 

PLAYERSTARTY = WINHEIGHT - PLAYERSIZE # location up the screen the player obj starts at

def main():
    global FPSCLOCK, DISPLAYSURF, PLAYER_IMG, RAIL_IMG

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('BLIZZARD!')
    
    # load the image files
    PLAYER_IMG = pygame.image.load(PLAYERIMAGE)
    RAIL_IMG = pygame.image.load(RAILIMAGE)
    
    while True:
        runGame()

def runGame():

    global railImages, railPositions, railnumber
    
    # Initialize all data structs
    playerObj = {'surface': pygame.transform.scale(PLAYER_IMG,
                                                    (PLAYERSIZE, PLAYERSIZE)),
        'x' : CENTER_RAIL,
        'y' : PLAYERSTARTY,
        'size' : PLAYERSIZE }
    
    railPositions = []
    railPositions.append(LEFT_RAIL)
    railPositions.append(CENTER_RAIL)
    railPositions.append(RIGHT_RAIL)
    
    railImages = []
    for i in range(3):
        railImages.append(RAIL_IMG)
    railnumber = 1

    railObjs = []
    for i in range(3):
        rail = createNewRail(i)
        railObjs.append(rail)        

    # Initialize player movement vars used in main game loop
    moveLeft = False
    moveRight = False
        
    ##### Main Game Loop #####

    railtick = 1
    
    while True:
        # fill white background
        DISPLAYSURF.fill(SNOWBACKGROUND)

        # display player object
        playerObj['rect'] = pygame.Rect( (playerObj['x'],
                                        playerObj['y'],
                                        playerObj['size'],
                                        playerObj['size']) )
        DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])

        if railtick == RAILTICK:
        # display rails
            if railnumber == 9:
                railnumber = 1
            else:
                railnumber += 1
            railtick = 0
        nextrail = pygame.image.load(RAILIMAGES % railnumber)
        
        for rail in railObjs:
            DISPLAYSURF.blit(nextrail, rail['rect'])

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            # determine direction pressed by user
            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    if playerObj['x'] != LEFT_RAIL:
                        moveLeft = True
                        moveRight = False
                    else:
                        moveLeft = False
                        moveRight = False
                elif event.key in (K_RIGHT, K_d):
                    if playerObj['x'] != RIGHT_RAIL:
                        moveLeft = False
                        moveRight = True
                    else:
                        moveLeft = False
                        moveRight = False

                # move player one rail over in direction of keypress
                if moveLeft:
                    playerObj['x'] -= RAIL
                if moveRight:
                    playerObj['x'] += RAIL

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        railtick += 1
            
def terminate():
    pygame.quit()
    sys.exit()

def createNewRail(i):
    newrail = {}
    newrail['width'] = RAILWIDTH
    newrail['height'] = RAILHEIGHT
    newrail['x'] = railPositions[i]
    newrail['y'] = 0
    newrail['rect'] = pygame.Rect( (newrail['x'], newrail['y'],
                                    newrail['width'], newrail['height']) )

    return newrail
    
if __name__ == '__main__':
    main()

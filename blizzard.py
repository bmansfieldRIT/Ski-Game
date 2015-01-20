"""	File: Blizzard.py
	Author: Brian Mansfield
	This file is the game loop, the main logic of the game and
	object interactions go here.
"""

import pygame, sys, time, math, random
from pygame.locals import *
from window_constants import *
from game_constants import *
from constructors import *

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('BLIZZARD!')
    
    while True:
        runGame()

def runGame():
    global railImages, railPositions, railnumber
    
    # load the image files
    PLAYER_IMG = pygame.image.load(PLAYERIMAGE)
    RAIL_IMG = pygame.image.load(RAILIMAGE)
    LTREELINE_IMG = pygame.image.load(LTREELINEIMAGE)
    RTREELINE_IMG = pygame.image.load(RTREELINEIMAGE)
    TREE_IMG = pygame.image.load(TREEOBSTACLEIMAGE)
    ZEROHEARTS_IMG = pygame.image.load(ZEROHEARTSIMAGE)
    ONEHEART_IMG = pygame.image.load(ONEHEARTIMAGE)
    TWOHEARTS_IMG = pygame.image.load(TWOHEARTSIMAGE)
    THREEHEARTS_IMG = pygame.image.load(THREEHEARTSIMAGE)
    GAMEOVER_IMG = pygame.image.load(GAMEOVERIMAGE)
    
    # Initialize all data structs
    player = {'surface': pygame.transform.scale(PLAYER_IMG,
                                                (PLAYERWIDTH, PLAYERHEIGHT)),
        'x' : PLAYERSTARTX,
        'y' : PLAYERSTARTY,
        'height' : PLAYERHEIGHT,
        'width' : PLAYERWIDTH,
        'health' : STARTHEALTH }
    
    railImages = []
    for i in range(3):
        railImages.append(RAIL_IMG)
    railnumber = 1

    rails = []
    rails.append(createNewRail(LEFT_RAIL))
    rails.append(createNewRail(CENTER_RAIL))
    rails.append(createNewRail(RIGHT_RAIL))

    # Trees alongside the edge of the screen
    treelineS = []
    treelines.append(createNewTreeline(LTREELINE_IMG, 0))
    treelines.append(createNewTreeline(RTREELINE_IMG, WINWIDTH - 35))

    # Create Game Over Screen
    gameOverScreen = createGameOverScreen(GAMEOVER_IMG)
    
    numObstacles = 0
    
    # Tree obstacle
    Obstacles = []
    obstacle = createNewObstacle('tree', TREE_IMG, TREEHEIGHT, CENTER_RAIL)
    Obstacles.append(obstacle)

    Hearts = []
    Hearts.append(ZEROHEARTS_IMG)
    Hearts.append(ONEHEART_IMG)
    Hearts.append(TWOHEARTS_IMG)
    Hearts.append(THREEHEARTS_IMG)

    obstaclesOnField = []
    # DEBUG
    obstaclesOnField.append(Obstacles[0])
    
    # Initialize player movement vars used in main game loop
    moveLeft = False
    moveRight = False
        
    ##### Main Game Loop #####

    railtick = 1
    obstacletick = 1
    gameOverStartTime = 0
    
    while True:
        
        # Display all images related to the main playing field
        DISPLAYSURF.fill(SNOWBACKGROUND)
        for treeline in treelines:
            DISPLAYSURF.blit(treeline['image'], treeline['rect'])
        for rail in rails:
                DISPLAYSURF.blit(rail['image'], rail['rect'])

        # Display player UI
        DISPLAYSURF.blit(Hearts[player['health']], pygame.Rect( (HEARTSXOFFSET,
                                                        HEARTSYOFFSET,
                                                        HEARTSWIDTH,
                                                        HEARTSHEIGHT) ))
        # Display obstacles on field
        for obstacle in Obstacles:
                DISPLAYSURF.blit(obstacle['image'], obstacle['rect'])

        # Display Game Over screen if condition is reached
        # CAUTION: MUST ALWAYS  BE LAST SURFACE DISPLAYED
        if player['health'] == 0:
            DISPLAYSURF.blit(gameOverScreen['image'], gameOverScreen['rect'])
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                terminate()

        # Collision detector
        if obstacle['x'] == player['x'] and (obstacle['y'] + obstacle['height']) == player['y']:
            player['health'] -= 1

        # Determine if game over condition is reached, set gameOverStartTime
        # to current time
        if player['health'] == 0 and gameOverStartTime == 0:
            gameOverStartTime = time.time()
                
        # Move obstacle on field
        if obstacletick == OBSTACLECHANGE:
            for obstacle in obstaclesOnField:
                obstacle['y'] += 1
                obstacle['rect'] = pygame.Rect( (obstacle['x'],
                                                 obstacle['y'],
                                                 obstacle['width'],
                                                 obstacle['height']) )
            obstacletick = 0 # reset the clock on moving obstacles

        # Load next rail image for animated effect
        if railtick == RAILCHANGE:
            if railnumber == 9:
                railnumber = 1
            else:
                railnumber += 1
                
            railtick = 0 # reset the clock on moving rails
            
            for rail in rails:
                rail['image'] = pygame.image.load(RAILIMAGES % railnumber)
        
        ##### EVENT HANDLING LOOP #####
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            # determine direction pressed by user
            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    if player['x'] != LEFT_RAIL + RAILWIDTH:
                        moveLeft = True
                        moveRight = False
                    else:
                        moveLeft = False
                        moveRight = False
                elif event.key in (K_RIGHT, K_d):
                    if player['x'] != RIGHT_RAIL + RAILWIDTH:
                        moveLeft = False
                        moveRight = True
                    else:
                        moveLeft = False
                        moveRight = False
                # Catch invalid keypress
                elif event.key in (K_UP, K_w, K_DOWN, K_s):
                    moveLeft = False
                    moveRight = False

                # move player one rail over in direction of keypress
                if moveLeft:
                    player['x'] -= RAIL
                if moveRight:
                    player['x'] += RAIL            
                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        # Update clocks used by game
        railtick += 1
        obstacletick += 1
            
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
